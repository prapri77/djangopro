from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg="<h1>This is my First Django framework</h1>"
    return(HttpResponse(msg))

def login(request):
    msg="<h1>Welcome to login page</h1>"
    return HttpResponse(msg)

def contact(request):
    msg="<h1>Welcome to contact page</h1>"
    return HttpResponse(msg)


