# Generated by Django 2.2.1 on 2020-12-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeess',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jobss',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LearningListss',
            fields=[
                ('list_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_id', models.ManyToManyField(related_name='employee', to='task.Employeess')),
                ('job_id', models.ManyToManyField(related_name='job', to='task.Jobss')),
            ],
        ),
    ]