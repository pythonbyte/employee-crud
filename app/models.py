from django.db import models


class Employee(models.Model):
    email = models.EmailField(max_length=150, blank=False, null=False)
    job_role = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=30, blank=False, null=False)

    cep = models.CharField(max_length=8, blank=False, null=False)
    city = models.CharField(max_length=50, blank=True, null=True)
    local_address = models.CharField(max_length=150, blank=True, null=True)
    neighborhood = models.CharField(max_length=50, blank=True, null=True)
    number = models.PositiveIntegerField(blank=False, null=False)
    state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
