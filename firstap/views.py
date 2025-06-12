from django.shortcuts import render
from django.http import HttpResponse
from .forms import CountryForm, ProvinceForm

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

def add_country(request):
    add_country_form = CountryForm()
    context = {
        "form" : add_country_form,
        "title" : "Country | Add Page"
    }
    return render(request, "add_country.html", context)

def add_province(request):
    add_province_form = ProvinceForm()
    context = {
        "form" : add_province_form,
        "title": "Province | Add Page"
    }
    return render(request, "add_province.html", context)
def province(request):
    context = {
        "province_name": "Bagmati",
        "province_code" : "Province Number One"
    }
    return render(request, "province.html", context)