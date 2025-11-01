# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Product, Profile
from .forms import FarmerRegisterForm, ConsumerRegisterForm, ProductForm

def home(request):
    """Home page displaying products by category"""
    fruits = Product.objects.filter(category='fruits')
    vegetables = Product.objects.filter(category='vegetables')
    dairy = Product.objects.filter(category='dairy')
    grains = Product.objects.filter(category='grains')

    context = {
        'fruits': fruits,
        'vegetables': vegetables,
        'dairy': dairy,
        'grains' : grains, 
    }
    return render(request, 'shop/home.html', context)

def about(request):
    """About page"""
    return render(request, 'shop/about.html')

def contact(request):
    """Contact page"""
    return render(request, 'shop/contact.html')

def farmer_register(request):
    """Farmer registration view"""
    if request.method == 'POST':
        form = FarmerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Farmer registration successful!')
            return redirect('farmer_dashboard')
    else:
        form = FarmerRegisterForm()
    return render(request, 'shop/farmer_register.html', {'form': form})

def consumer_register(request):
    """Consumer registration view"""
    if request.method == 'POST':
        form = ConsumerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Consumer registration successful!')
            return redirect('consumer_dashboard')
    else:
        form = ConsumerRegisterForm()
    return render(request, 'shop/consumer_register.html', {'form': form})

def logout_user(request):
    """Custom logout view"""
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully!')
    return redirect('home')

@login_required
def farmer_dashboard(request):
    """Farmer dashboard showing their products"""
    try:
        profile = request.user.profile
        if profile.role != 'farmer':
            messages.error(request, 'Access denied. Farmers only.')
            return redirect('home')
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('home')
    
    products = Product.objects.filter(farmer=request.user)
    return render(request, 'shop/farmer_dashboard.html', {'products': products})

@login_required
def consumer_dashboard(request):
    """Consumer dashboard"""
    try:
        profile = request.user.profile
        if profile.role != 'consumer':
            messages.error(request, 'Access denied. Consumers only.')
            return redirect('home')
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('home')
    
    return render(request, 'shop/consumer_dashboard.html')

@login_required
def add_product(request):
    """Add product view for farmers"""
    try:
        profile = request.user.profile
        if profile.role != 'farmer':
            messages.error(request, 'Only farmers can add products.')
            return redirect('home')
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('farmer_dashboard')
    else:
        form = ProductForm()
    
    return render(request, 'shop/add_product.html', {'form': form})

def cart_view(request):
    """Display cart contents"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            subtotal = product.price * qty
            cart_items.append({
                'product': product,
                'qty': qty,
                'subtotal': subtotal
            })
            total += subtotal
        except Product.DoesNotExist:
            continue
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)

def add_to_cart(request, product_id):
    """Add product to cart"""
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, id=product_id)
            cart = request.session.get('cart', {})
            
            if str(product_id) in cart:
                cart[str(product_id)] += 1
            else:
                cart[str(product_id)] = 1
                
            request.session['cart'] = cart
            request.session.modified = True  # Force session save
            messages.success(request, f'{product.name} added to cart!')
            
            # Redirect to cart page instead of home
            return redirect('view_cart')
        except Exception as e:
            messages.error(request, 'Error adding product to cart.')
            return redirect('home')
    
    return redirect('home')

def remove_from_cart(request, product_id):
    """Remove product from cart or decrease quantity"""
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        if request.method == 'POST':
            # Decrease quantity by 1
            cart[product_id_str] -= 1
            if cart[product_id_str] <= 0:
                del cart[product_id_str]
        else:
            # Remove completely (for GET requests)
            del cart[product_id_str]
        
        request.session['cart'] = cart
        messages.success(request, 'Cart updated!')
    
    return redirect('view_cart')

@login_required
def checkout(request):
    """Checkout page"""
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, 'Your cart is empty.')
        return render(request, 'shop/checkout.html', {'message': 'Your cart is empty.'})
    
    cart_items = []
    total = 0
    
    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            subtotal = product.price * qty
            cart_items.append({
                'product': product,
                'qty': qty,
                'subtotal': subtotal
            })
            total += subtotal
        except Product.DoesNotExist:
            continue
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/checkout.html', context)

@login_required
def place_order(request):
    """Place order and clear cart"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        if not cart:
            messages.warning(request, 'Your cart is empty.')
            return redirect('view_cart')
        
        # Here you would typically save the order to database
        # For now, we'll just clear the cart and show confirmation
        
        request.session['cart'] = {}
        messages.success(request, 'Order placed successfully!')
        return render(request, 'shop/order_confirmation.html')
    
    return redirect('checkout')