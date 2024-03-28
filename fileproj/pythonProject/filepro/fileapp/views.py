from django.shortcuts import render
from django.http import HttpResponse
from .functions import handle_uploaded_file
from .forms import StudentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded succcessfully")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form': student})
