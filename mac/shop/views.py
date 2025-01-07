from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n // 4 + ceil((n/4) - (n//4))
    # params = {'no_of_slides':nslides,'range':range(1,nslides), 'product': products}
    allProds = []
    catprods = Product.objects.values('category','id')
    cat = {item['category'] for item in catprods }
    for cat in cat:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nslides), nslides])
     
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params )
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    #Fetch product using id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html',{'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html') 

def productlist(request):
    context = {'product':Product.objects.all()}
    return render(request, 'shop/products.html',context)