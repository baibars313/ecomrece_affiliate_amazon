from django.shortcuts import render
from .models import *


def home(request):
    all_cats=Category.objects.all()
    return render(request,'home.html',{"all_cats":all_cats})

def all_products(request,catid):
    all_prod=Products.objects.filter(category=catid)
    all_cats=Category.objects.all()
    return render(request,'category.html', {'all_prods':all_prod,'all_cats':all_cats})