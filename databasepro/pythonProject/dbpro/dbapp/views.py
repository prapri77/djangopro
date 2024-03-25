from django.shortcuts import render, redirect
from . form import EmployeeForm
from . models import Employee
from . models import Student


# Create your views here.

def home(request):
    mydata = Employee.objects.all()
    if(mydata!=''):
        return render(request,"index.html",{"datas": mydata})
    else:
        return render(request, "index.html")

def adddata(request):
    if request.method == "POST":
        eid = request.POST['eid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']

        obj = Employee()
        obj.eid = eid
        obj.name = name
        obj.contact = contact
        obj.address = address
        obj.save()
        mydata = Employee.objects.all()
        return redirect("home")

    return render(request, 'index.html')

def updatedata(request,id):
    mydata = Employee.objects.get(id=id)
    if request.method == "POST":
        eid = request.POST['eid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']
        mydata.eid = eid
        mydata.name = name
        mydata.contact = contact
        mydata.address = address
        mydata.save()
        return redirect("home")
    return render(request, 'update.html',{'data': mydata})
def deletedata(request,id):
    mydata = Employee.objects.get(id=id)
    mydata.delete()
    return redirect("home")


def stu(request):
    if request.method == "POST":
        sid = request.POST['sid']
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']

        obj1 = Student()
        obj1.sid = sid
        obj1.name = name
        obj1.contact = contact
        obj1.address = address
        obj1.save()
    return render(request, 'student.html')

