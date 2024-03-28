from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response
def getcookie(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: " + tutorial);


import csv


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    return response
