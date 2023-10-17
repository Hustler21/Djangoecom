from django.shortcuts import render,get_object_or_404

from category.models import Category
from store.models import Product

# Create your views here.
def category_details(request):
    products = Category.objects.all().filter(is_available=True).order_by('id')
    context={
        'products':products,
    }
    return render(request, 'category.html',context)


def category_product(request, category_slug):  
    categories = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=categories, is_available=True)
       
    context={
        'products':products,
    }
    return render(request, 'category copy.html',context)


def category_product_detail(request,category_slug,product_slug,):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context={
        'single_product':single_product,
    }
    return render(request, 'product_detail.html',context )