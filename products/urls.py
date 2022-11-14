from django.urls import path
from .views import product_list , product_detail, new_product, edit_product,delet_product

app_name='products'

urlpatterns = [
    path('', product_list,name='product_list'),
    path('new/', new_product,name='new_product'),
    path('<int:id>', product_detail,name='product_detail'),
     path('<int:id>/edit', edit_product,name='edit_product'),
      path('<int:id>/delete', delet_product,name='delete_product'),
]