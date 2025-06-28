from django.shortcuts import render
from app.models import Employee
# Create your views here.
from django.shortcuts import render   

from django.http import HttpResponse
def home(request):
    employees=Employee.objects.all()
    context={
        'employees':employees
    }
    return render(request,'home.html',context)



def contact(request):
    return render(request,'contact.html')