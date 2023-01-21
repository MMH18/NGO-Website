from django.urls import path
from products.views import list_products,create_product,update_product,delete_product



app_name = 'products'
urlpatterns = [
    path('',list_products, name='list_products'),
    path('create/',create_product, name='create_product'),
    path('update/<int:prod_id>/',update_product, name='update_product'),
    path('delete/<int:prod_id>/',delete_product, name='delete_product'),

]