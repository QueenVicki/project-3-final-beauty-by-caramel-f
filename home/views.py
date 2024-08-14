from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Beauty for your needs!")

def index(request):
     return render(request,"home.html")

def about(request):
     return render(request,"about.html")

def services(request):
    return HttpResponse("Our Services page!")

def book(request):
    return HttpResponse("Book your appointment today!")