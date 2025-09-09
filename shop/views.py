from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# ----------------------------
# Home Page
# ----------------------------
def home(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    fruits = Product.objects.filter(category='fruits')
    vegetables = Product.objects.filter(category='vegetables')
    dairy = Product.objects.filter(category='dairy')

    context = {
        'fruits': fruits,
        'vegetables': vegetables,
        'dairy': dairy,
    }
    return render(request, 'shop/home.html', context)


def about(request):
    return render(request, 'shop/about.html')


def dashboard(request):
    return render(request, 'shop/farmer_dashboard.html')


def contact(request):
    return render(request, 'shop/contact.html')


# ----------------------------
# Cart Views
# ----------------------------
def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * qty
        products.append({"product": product, "qty": qty, "subtotal": subtotal})
        total += subtotal

    return render(request, "shop/cart.html", {"cart_items": products, "total": total})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    return redirect('view_cart')


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return render(request, "shop/checkout.html", {"message": "Your cart is empty!"})

    products = []
    total = 0
    for product_id, qty in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * qty
        products.append({"product": product, "qty": qty, "subtotal": subtotal})
        total += subtotal

    return render(request, "shop/checkout.html", {"cart_items": products, "total": total})


def place_order(request):
    request.session['cart'] = {}
    return render(request, "shop/order_confirmation.html")


# ----------------------------
# Authentication
# ----------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "shop/register.html", {"form": form})


@require_POST
def logout_user(request):
    logout(request)
    return redirect("home")


# ----------------------------
# Farmer Add Product
# ----------------------------
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            return redirect("dashboard")
    else:
        form = ProductForm()
    return render(request, "shop/add_product.html", {"form": form})
