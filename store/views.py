from django.shortcuts import render

from store.models import Product

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')
    context={
        'products':products,
    }
    return render(request, 'store.html',context )

def product_detail(request,product_slug):
    single_product = Product.objects.get( slug=product_slug)
    context={
        'single_product':single_product,
    }
    return render(request, 'product_detail.html',context )