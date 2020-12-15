from customer.views import sign_up
from django.urls import path

urlpatterns = [
    path('signup',sign_up),
]
