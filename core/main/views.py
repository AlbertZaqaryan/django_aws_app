from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.
def home(request):
    category = Category.objects.all()
    return render(request, 'main/index.html', context={
        'category_List':category
    })


