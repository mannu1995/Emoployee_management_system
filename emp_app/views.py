from django.db.models import Q
from django.shortcuts import render,HttpResponse
from .models import Department,Role,Employee
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')
def all_emp(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    print(context)
    return render(request, 'all_emp.html',context)

def add_emp(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {'departments': departments, 'roles':roles}
        return render(request, 'add_emp.html',context)

    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        role = request.POST['role']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone_number = int(request.POST['phone_number'])
        new_emp = Employee(first_name=first_name,last_name=last_name,department_id=department,role_id=role,salary=salary,phone_number=phone_number,bonus=bonus,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added')
    else:
        return render(request, 'add_emp.html')

def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(employee_id=emp_id)
            emp_to_remove.delete()
            return HttpResponse(f'Employee {emp_to_remove.first_name} has been deleted successfully.')
        except:
            return HttpResponse('llll')

    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'remove.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        employees = Employee.objects.all()
        print(employees)
        if name:
            employees = employees.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if department:
            employees = employees.filter(department_id=department)
        if role:
            employees = employees.filter(role_id=role)
        context = {'employees':employees}
        print(context)
        return render(request, 'all_emp.html',context)
    else:
        return render(request, 'filter.html')

