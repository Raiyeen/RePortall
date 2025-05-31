from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request, "index.html")


def aboutUs(request):
     return render(request, "aboutUs.html")
 
def contactUs(request):
     return render(request, "contactUs.html")