from django.shortcuts import render
from . form import EmployeeForm
from . models import Employee
from . models import Student


# Create your views here.
def emp(request):
    if request.method == "POST":
        eid = request.POST['eid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']

        obj = Employee();
        obj.eid = eid
        obj.name = name
        obj.contact = contact
        obj.address = address
        obj.save()
    return render(request, 'index.html')

def stu(request):
    if request.method == "POST":
        sid = request.POST['sid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']

        obj1 = Student();
        obj1.sid = sid
        obj1.name = name
        obj1.contact = contact
        obj1.address = address
        obj1.save()
    return render(request, 'student.html')

