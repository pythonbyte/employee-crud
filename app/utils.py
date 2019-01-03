import requests

from rest_framework.exceptions import ValidationError


class Cache():

    def __init__(self):
        self._cache_list = []

    @property
    def cache_list(self):
        return self._cache_list

    @cache_list.setter
    def cache_list(self, value):
        # setting the maximum size of the cache
        if len(self.cache_list) > 20:
            # if the cache has more than 20 zipcodes delete the oldest one
            del self.cache_list[0]
        self._cache_list.append(value)
    #
    @cache_list.deleter
    def cache_list(self):
        del self.cache_list



cache = Cache()
def get_address(obj):
    # base url to retrieve the address after sending the zipcode
    cep_url = 'http://127.0.0.1:8080/getzipcode/{}'

    # getting the zipcode from the object
    cep = obj['cep']

    try:
        # iterating over the Cache to verify if zipcode was already used
        cached_address = next(
            item for item in cache.cache_list if item["cep"] == cep
        )
        # setting the number from the request
        cached_address['number'] = obj['number']
        return cached_address

    except Exception:
        # using pass to fix the "stop iteration" error that comes from the next
        # iterator
        pass

    # sending the request to get the address using the zipcode
    cep_resp = requests.post(cep_url.format(cep))

    # treating the error
    if cep_resp.status_code == 400:
        raise ValidationError(cep_resp.json())

    try:
        # getting only the json data from the request
        cep_resp = cep_resp.json()

        # serializing the data
        address = {
            'cep': cep,
            'number': obj['number'],
            'city': obj.get('city') or cep_resp['city'],
            'state': obj.get('state') or cep_resp['state'],
            'local_address': obj.get('local_address') or cep_resp['address'],
            'neighborhood': (
                obj.get('neighborhood') or cep_resp['neighborhood']
            )
        }
        cache.cache_list = address
        return address

    except Exception as e:
        raise ValidationError({'error': e})

