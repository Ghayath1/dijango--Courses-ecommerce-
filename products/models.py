from statistics import quantiles
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=5000)
    quantity=models.IntegerField()
    price=models.FloatField()
    image=models.ImageField(upload_to='products/')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='product_category')

    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

        
    class Meta:
        verbose_name ='Category'
        verbose_name_plural ='Categories'


class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='review_auhtor')
    product =models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_review')
    rate = models.IntegerField()
    review = models.TextField(max_length=500)
    created_at =models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user)
    

  