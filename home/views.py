from django.shortcuts import render, HttpResponse

# Create your views here.
def home(index):
    return HttpResponse('Home')

def about(index):
    return HttpResponse('about')

def contact(index):
    return HttpResponse('contact')
