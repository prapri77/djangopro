from django.shortcuts import render

# Create your views here.
def extend(request):
    return render(request,'extend.html')

def loopex(request):
    context ={
        "data" :[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'loop.html',context)

def include(request):
    return render(request,'include.html')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def time(request):
    return render(request,'time.html')

def first(request):
    context = {
        "var1" : None,
        "var2": None,
        "var3": "Django framework"
    }
    return render(request,"first.html",context)