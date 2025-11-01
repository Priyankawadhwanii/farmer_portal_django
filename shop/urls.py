# shop/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # registration
    path('register/farmer/', views.farmer_register, name='farmer_register'),
    path('register/consumer/', views.consumer_register, name='consumer_register'),

    # login/logout
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),  # POST logout form

    # dashboards
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('consumer/dashboard/', views.consumer_dashboard, name='consumer_dashboard'),

    # cart & orders & product
    path('cart/', views.cart_view, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),
    path('add_product/', views.add_product, name='add_product'),
]
