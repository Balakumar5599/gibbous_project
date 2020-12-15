from django.db import models


# Create your models here.
class Employeess(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)


class Jobss(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=200)


class LearningListss(models.Model):
    list_id = models.IntegerField(primary_key=True)
    emp_id = models.ManyToManyField(Employeess, related_name='employee')
    job_id = models.ManyToManyField(Jobss, related_name='job')
