from django.contrib import admin

# Register your models here.
from .models import Product, Category,ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','price']
    list_filter = ['quantity','category','price']
    search_fields = ['name','desc']




class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','rate']



admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductReview,ReviewAdmin)