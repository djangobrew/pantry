from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50,)
    job = models.CharField(max_length=50,)
    hired_on = models.DateField(auto_now_add=True,)

    def __str__(self):
        return f'Employee("{self.first_name}", "{self.last_name}")'
