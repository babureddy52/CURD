from django.db import models

class Employee1(models.Model):
    EmpId=models.IntegerField(primary_key=True)
    EmpName=models.CharField(max_length=20)
    Salary=models.IntegerField()
    Edit=models.CharField(max_length=10)
    Delete=models.CharField(max_length=10)


class Employee(models.Model):
    Eid = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=20)
    Phno = models.CharField(max_length=15)
    Salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return self.Ename