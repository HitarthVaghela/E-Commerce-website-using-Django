from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return HttpResponse('about')

def contact(request):
    return HttpResponse('contact')
