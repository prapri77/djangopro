from django.shortcuts import render
from django.views import generic


# Create your views here.
def demo(request):
    return render(request, 'index.html')
