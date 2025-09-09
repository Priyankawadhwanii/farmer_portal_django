from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Cart
    path('cart/', views.cart_view, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),

    # Farmer
    path('add_product/', views.add_product, name='add_product'),
]
