
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<str:id>', views.productview, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('search/', views.productsearch, name='search'),
    path('cart/', views.view_cart, name='cart'),
    path('category/<int:cat_id>', views.category, name='category'),
    path('accounts/login/', views.loginn, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),

]