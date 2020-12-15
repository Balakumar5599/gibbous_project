from django.shortcuts import render
from .models import Customer
from django.db import connection
from django.contrib.auth.models import User
from tenant_schemas.utils import tenant_context

def sign_up(request):
    if request.method == "POST":
        tenant=Customer(domain_url=request.POST.get('domain_url'),schema_name=request.POST.get('schema_name'),name=request.POST.get('name'))
        tenant.save()
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        with tenant_context(tenant):
            User.objects.create_superuser(username=username, password=password, email=email)

        return render(request,"tenant_sign.html")
    else:
        return render(request,"tenant_sign.html")