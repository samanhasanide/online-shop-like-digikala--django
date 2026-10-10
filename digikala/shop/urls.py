
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('product/<int:pk>', views.product_pages, name='product_page'),
    path('category/<str:cat>', views.category_page, name='category_page'),
    path('categories/', views.category_summary, name='category_summary'),
    path('checkout/', views.checkout, name='checkout'),




]
