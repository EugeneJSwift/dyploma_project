
from django.urls import path
from goods import views


app_name = 'goods'

urlpatterns = [
    # path('', views.catalog, name = 'index'),
    path('catalog_category/', views.catalog_category, name = 'catalog_category'),
    path('catalog_category/<slug:category_slug>/', views.catalog_category, name='catalog_category_by_slug'),
    path('product/<slug:product_slug>/', views.product, name = 'product'),
     path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    # path('about', views.about, name = 'about')
]
