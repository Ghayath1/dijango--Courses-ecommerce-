from django.shortcuts import render,redirect
from .models import Product, Category, ProductReview
from .forms import ProductForm

# Create your views here.

def product_list(request):
    objects = Product.objects.all
    return render(request,'products/list.html',{'product_list':objects})


def product_detail(request,id):

    object = Product.objects.get(id=id)
    reviews = ProductReview.objects.filter(product=object)
    return render(request,'products/detail.html', {
        'product': object,
        'product_reviews' : reviews
    })


def new_product(request):
    if request.method =='POST':
      form = ProductForm(request.POST,request.FILES)
      if form.is_valid():
          form.save()
          return redirect('/products/')

    else:
        form = ProductForm()
    return render(request,'products/new.html',{'form':form})

def edit_product(request,id):
    object = Product.objects.get(id=id)
    if request.method =='POST':
      form = ProductForm(request.POST,request.FILES, instance=object)
      if form.is_valid():
          form.save()
          return redirect('/products/')

    else:
        form = ProductForm(instance=object)
    return render(request,'products/edit.html',{'form':form})


def delet_product(request,id):
    object = Product.objects.get(id=id)
    object.delete()
    return redirect('/products/')