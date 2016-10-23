from django.shortcuts import render
from django.http import HttpResponse

from models import Employee

# Create your views here.

def index(request):
    employee = Employee.objects.create(
        email = 'deep.rnj@gmail.com',
        first_name = 'deepak',
        last_name = 'kumar'
    )
    employee.save()
    return HttpResponse({'hi': 'hello'})
