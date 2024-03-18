from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'index.html')

def index(request):
    return render (request,'index1.html')

def home(request):
    return render (request,'home.html')

def nameview(request):
    # create a dictionary
    context = {
        "first_name" : "Naveen",
        "last_name"  : "Arora",
    }
    # return response
    return render(request, "nameview.html", context)

def check_age(request):
    if request.method == 'POST':
      # Get the age from the form
        age = int(request.POST.get('age', 0))
        return render(request, 'checkage.html', {'age': age})
    return render(request, 'checkage.html')





