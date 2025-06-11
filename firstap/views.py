from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("Hello! this is my first django app")

def country(request):
    context = {
        "country_name" : "Nepal",
        "continent" : "Asia",
        "country_code": "+977"
    }
    return render(request, "country.html", context)

def province(request):
    context = {
        "province_name": "Bagmati",
        "province_code" : "Province Number One"
    }
    return render(request, "province.html", context)