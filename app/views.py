from django.shortcuts import render,get_object_or_404,redirect
from app.models import Employee
from django.http import HttpResponse
from django.contrib import messages


def employee_details(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    context ={
        'employee':employee
    }
    return render(request,'details.html',context)



def add(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        photo = request.FILES.get('photo')

        # Optional: you can add validation here if needed
        try:
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                designation=designation,
                email_address=email_address,
                phone_number=phone_number,
                photo=photo
            )
            messages.success(request, "Employee added successfully!")
            return redirect('home')  # Or 'home'
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    
    return render(request, 'form.html')



def delete(request,id):
    employee=get_object_or_404(Employee,id=id)
    employee.delete()

    return redirect('home')
