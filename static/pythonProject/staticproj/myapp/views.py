from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return render(request, 'myapp/index.html')

