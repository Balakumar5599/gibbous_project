from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
import requests
from tenant_schemas.utils import schema_context
from django.contrib.auth import authenticate
from customer.models import Customer
from rest_framework.response import Response
from rest_framework import response
from task.models import Employeess, Jobss, LearningListss
from task.serializers import EmployeeSerializer, TaskSerializer, LearningSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, FormParser

@api_view(['POST'])
def login(request):
    user_data=JSONParser().parse(request)
    domain_url=request.get_raw_uri().split('//')[1].split(':')[0]
    schema_name=Customer.objects.filter(domain_url=domain_url).all()
    schema=[]
    for i in schema_name:
        schema.append(i.schema_name)
    with schema_context(schema[0]):
        user = authenticate(username=user_data['username'],password=user_data['password'])

    if user is not None:
        request.session.__setitem__('username', user_data['username'])
        return JsonResponse({'mes': 'ryt'})
    else:
        return JsonResponse({'message': 'wrong'})

@api_view(['DELETE'])
def logout(request):
    try:
        request.session.__delitem__('username')
        return JsonResponse({'message':'Successfully logged out'})
    except KeyError:
        pass
    return redirect(login)

@api_view(['GET', 'POST'])
def tenant_view(request):
    if 'username' in request.session:
        if request.method == 'GET':
            employee = Employeess.objects.all()
            jobs = Jobss.objects.all()
            learnings = LearningListss.objects.all()
            emp_serializer = EmployeeSerializer(employee, many=True)
            job_serializer = TaskSerializer(jobs, many=True)
            learning_serializer = LearningSerializer(learnings, many=True)
            return Response({"emp": emp_serializer.data, "job": job_serializer.data,
                             "list": learning_serializer.data})  # JsonResponse(job_serializer.data,safe=False)
    else:
        return Response({"MESSAGE":"LOGIN FIRST"})


'''
            emp={
                "emps":emps
            }
            task={
                "task":tasks
            }
            return render(request,"emp_page.html")
'''


@api_view(['POST'])
def add_employee(request):
    if 'username' in request.session:
        if request.method == 'POST':
            emp_data = JSONParser().parse(request)
            emp_serializer = EmployeeSerializer(data=emp_data)
            if emp_serializer.is_valid():
                emp_serializer.save()
                return JsonResponse({'message': 'Added Successfully'})
            return JsonResponse({'message': 'wrong'})
    else:
        return Response({"MESSAGE":"LOGIN FIRST"})


'''
            emp=Employeess()
            emp.emp_id=request.POST.get('emp_id')
            emp.emp_name=request.POST.get('emp_name')
            emp.save()
            emps=Employeess.objects.all()
            emp={
                "emp":emps
            }list_data=JSONParser().parse(request)
            list_serializer=LearningSerializer(data=list_data)
            if list_serializer.is_valid():
                list_serializer.save()
                return JsonResponse(list_serializer.data)
            return JsonResponse({'message':'wrong'})
            return render(request,'add_emp.html',emp)
        return render(request,'add_emp.html')
'''


@api_view(['POST'])
def add_task(request):
    if 'username' in request.session:
        if request.method == "POST":
            job_data = JSONParser().parse(request)
            job_serializer = TaskSerializer(data=job_data)
            if job_serializer.is_valid():
                job_serializer.save()
                return JsonResponse(job_serializer.data)
            return JsonResponse({'message': 'wrong'})
    else:
        return Response({"MESSAGE":"LOGIN FIRST"})

'''
            task=Jobss()
            task.job_id=request.POST.get('job_id')
            task.job_name=request.POST.get('job_name')
            task.job_description=request.POST.get('job_description')
            task.save()
            tasks=Jobss.objects.all()
            task={
                "task":tasks
            }
            return render(request,'add_task.html',task)
        return render(request,'add_task.html')
'''


@api_view(['POST'])
def provide_task(request):
    if 'username' in request.session:
        if request.method == "POST":
            learning_data = JSONParser().parse(request)
            learning_obj = LearningListss()
            learning_obj.list_id = learning_data['list_id']
            learning_obj.save()
            for i in learning_data['emp_id']:
                learning_obj.emp_id.add(i)
            for i in learning_data['job_id']:
                learning_obj.job_id.add(i)
            learning_obj.save()
            return Response({"message": "Added"})
    else:
        return Response({"MESSAGE": "LOGIN FIRST"})

            # list_data = JSONParser().parse(request)
            # learning=LearningListss.objects.create(list_id=list_data['list_id'])
            # emp=Employeess(emp_id=list_data['emp_id'])
            # job=Jobss(job_id=list_data['job_id'])
            # learning.emp_id.add(emp)
            # learning.job_id.add(job)
            # learning.save()
            # ls=LearningSerializer(learning,many=True)
            # return JsonResponse({"ls": ls})

            # learning_obj = LearningListss()
            # learning_obj.list_id = list_id
            # learning_obj.save()
            # learning_obj.emp_id.add(emp_id)
            # learning_obj.job_id.add(job_id)
            # learning_obj.save()
            # l = LearningListss.objects.all()
            # ls = LearningSerializer(l,many=True)
            # return JsonResponse({"ls" :ls})

            # list_serializer=LearningSerializer(data=list_data)
            # list_serializer.save()
            # print(list_serializer)
            # return JsonResponse({'message': 'added'})


'''

            learning_data = JSONParser().parse(request)
            learning_obj=LearningListss()
            learning_obj.list_id=learning_data['list_id']
            learning_obj.save()
            learning_obj.emp_id.add(learning_data['emp_id'])
            learning_obj.job_id.add(learning_data['job_id'])
            learning_obj.save()
            
            #learning=LearningListss.objects.all()
            #learning_serializer=LearningSerializer(learning,many=True)
            
            return JsonResponse({"message": "Added"})
'''


def emp_view(request):
    if 'username' in request.session:
        schema = request.get_raw_uri()
        schema = schema.split('//')[1].split('.')[0]

        emp_json = {"emp_id": request.POST.get('emp_id'),
                    "emp_name": request.POST.get('emp_name')
                    }

        job_json = {"job_id": request.POST.get('job_id'),
                    "job_name": request.POST.get('job_name'),
                    "job_description": request.POST.get('job_description')
                    }
        assign_json = {
            'list_id': request.POST.get('list_id'),
            'emp_id': request.POST.get('emp_id'),
            'job_id': request.POST.get('job_id')
        }

        response1 = requests.get('http://{}.localhost:8000/tenant'.format(schema))
        response2 = requests.post('http://{}.localhost:8000/add_employee'.format(schema), json=emp_json)
        response3 = requests.post('http://{}.localhost:8000/add_task'.format(schema), json=job_json)
        response4 = requests.post('http://{}.localhost:8000/assign_task'.format(schema), json=assign_json)

        json_data1 = response1.json()
        json_data2 = response2.json()
        json_data3 = response3.json()
        # json_data4 = response4.json()
        # print(json_data4)

        return render(request, "index.html", {"json_data1": json_data1})
    else:
        return redirect(login)


'''
            learning=LearningListss()
            learning.list_id=request.POST.get('list_id')
            learning.save()
            learning.emp_id.add(request.POST.get('emp_id'))
            learning.job_id.add(request.POST.get('job_id'))
            
            learning.save()
            learnings=LearningListss.objects.all()

            learning={
                "learning":learnings
            }
            return render(request,'learnings.html',learning)
        return render(request,'learnings.html')
'''
'''
        elif request.method=='POST':
            list_data=JSONParser().parse(request)
            list_serializer=LearningSerializer(data=list_data)
            if list_serializer.is_valid():
                list_serializer.save()
                return JsonResponse(list_serializer.data)
            return JsonResponse({'message':'wrong'})
    else:
        return redirect(login)

@api_view(['GET'])
def learnings_list(request,emp_id):
    if 'username' in request.session:
        if request.method=='GET':
            learning=LearningLists.objects.filter(emp_id=emp_id).all()
            emp_serializer=LearningSerializer(learning,many=True)
            return JsonResponse(emp_serializer.data,safe=False)
    else:
        return redirect(login)
    

@api_view(['DELETE'])
def delete(request,list_id):
    if 'username' in request.session:
        delete_data=LearningLists.objects.filter(list_id=list_id).delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'})
    else:
        return redirect(login)



'''
