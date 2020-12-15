from rest_framework import serializers
from .models import Employeess, Jobss, LearningListss


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employeess
        fields = ('emp_id', 'emp_name')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobss
        fields = ('job_id', 'job_name', 'job_description')


class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningListss
        fields = ['list_id', 'emp_id', 'job_id']


'''
    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        job_data = validated_data.pop('job')
        lists = LearningListss.objects.create(**validated_data)
        lists.save()
        for employee in employee_data:
            emps = Employeess.objects.get_or_create(emp_id=employee['emp_id'])
            lists.employee.add(emps)
        for job in job_data:
            jobs=Jobss.objects.get_or_create(job_id=job['job_id'])
        return lists
'''
