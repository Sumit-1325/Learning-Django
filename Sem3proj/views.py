from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World its me sumit Home page ")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello World its me sumit About page  ")

def contact(request):
    return HttpResponse("Hello World its me sumit Contact page ")