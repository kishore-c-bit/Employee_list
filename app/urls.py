from django.urls import path
from . import views


urlpatterns=[
    
    path('<int:pk>/',views.employee_details,name='employee_d'),
    path('add/',views.add, name='add'),
    path('delete/<int:id>/',views.delete, name='delete'),
]

