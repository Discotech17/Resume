from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def AboutMe(request):
    return render(request, 'aboutme.html')

def Resume(request):
    return render(request, 'resume.html')

