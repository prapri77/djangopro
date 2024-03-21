from django.shortcuts import render,redirect

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def destination_view(request):
    return HttpResponse(
        'Home Function is redirected to destination_view function')
def home(request):
    return redirect('destination-view')

