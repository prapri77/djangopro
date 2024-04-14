from django.shortcuts import render, redirect
from django.views import generic



# Create your views here.
def demo(request):
    return render(request, 'index.html')


