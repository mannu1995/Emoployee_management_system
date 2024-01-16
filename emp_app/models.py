from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70,null=False)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name