from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TestGetCreateEmployee(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.valid_employee_data = {
            "name": "Teste do Teste",
            "email": "teste@hot.com",
            "job_role": "Developer",
            "phone": "31999999999",
            "cep": "30330330",
            "number": "15"
        }

        self.invalid_employee_data = {
            "name": "",
            "email": "teste@hot.com",
            "job_role": "Developer",
            "phone": "31999999999",
            "cep": "300330",
            "number": "15"
        }

        self.correct_return = {
            "id": 2,
            "cep": "30330330",
            "city": "Belo Horizonte",
            "email": "teste@hot.com",
            "job_role": "Developer",
            "local_address": "Rua Campo Belo",
            "name": "Teste do Teste",
            "neighborhood": "São Pedro",
            "number": 15,
            "phone": "31999999999",
            "state": "MG"
        }


    def test_get_employee_list(self):
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee_valid_data(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.valid_employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_invalid_data(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.invalid_employee_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_employee_valid_return(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.valid_employee_data)
        self.assertEqual(response.json(), self.correct_return)

    def test_wrong_method_endpoint(self):
        url = reverse('employee-list')
        response = self.client.put(url, data=self.valid_employee_data)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )


    def test_get_employee_detail(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.valid_employee_data)
        url = reverse('employee-detail', kwargs={'pk': response.json()['id']})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_employee(self):
        url = reverse('employee-list')
        response = self.client.post(url, data=self.valid_employee_data)
        url = reverse('employee-detail', kwargs={'pk': response.json()['id']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
