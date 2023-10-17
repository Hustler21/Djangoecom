from django.db import models
from django.urls import reverse

from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ManyToManyField(Category,)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    is_digital      = models.BooleanField(default=False)

    def get_url(self):
        return reverse('product_detail', args=[self.slug])
    

    def __str__(self):
        return self.product_name
