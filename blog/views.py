from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(index):
    return HttpResponse('BlogHome')

def blogPost(index):
    return HttpResponse('blogPost')
