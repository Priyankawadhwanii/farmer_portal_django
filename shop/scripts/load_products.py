import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "farmer_portal.settings")
django.setup()

from shop.models import Product

# List of products with category and price
products = [
    {"name": "apple", "category": "fruits", "price": 60},
    {"name": "banana", "category": "fruits", "price": 40},
    {"name": "orange", "category": "fruits", "price": 50},
    {"name": "mango", "category": "fruits", "price": 80},
    {"name": "grapes", "category": "fruits", "price": 120},
    {"name": "pineapple", "category": "fruits", "price": 90},
    {"name": "papaya", "category": "fruits", "price": 70},
    {"name": "strawberry", "category": "fruits", "price": 150},
    {"name": "watermelon", "category": "fruits", "price": 60},
    {"name": "kiwi", "category": "fruits", "price": 100},
    {"name": "carrot", "category": "vegetables", "price": 30},
    {"name": "tomato", "category": "vegetables", "price": 35},
    {"name": "potato", "category": "vegetables", "price": 25},
    {"name": "onion", "category": "vegetables", "price": 40},
    {"name": "cucumber", "category": "vegetables", "price": 30},
    {"name": "spinach", "category": "vegetables", "price": 25},
    {"name": "cauliflower", "category": "vegetables", "price": 50},
    {"name": "broccoli", "category": "vegetables", "price": 90},
    {"name": "capsicum", "category": "vegetables", "price": 70},
    {"name": "beetroot", "category": "vegetables", "price": 40},
    {"name": "milk", "category": "dairy", "price": 45},
    {"name": "paneer", "category": "dairy", "price": 120},
    {"name": "curd", "category": "dairy", "price": 50},
    {"name": "butter", "category": "dairy", "price": 90},
    {"name": "cheese", "category": "dairy", "price": 150},
    {"name": "ghee", "category": "dairy", "price": 250},
    {"name": "yogurt", "category": "dairy", "price": 60},
    {"name": "cream", "category": "dairy", "price": 80},
    {"name": "buttermilk", "category": "dairy", "price": 40},
    {"name": "ice cream", "category": "dairy", "price": 120},
    {"name": "chili", "category": "vegetables", "price": 30},
    {"name": "ginger", "category": "vegetables", "price": 60},
    {"name": "garlic", "category": "vegetables", "price": 50},
    {"name": "lemon", "category": "fruits", "price": 20},
    {"name": "mushroom", "category": "vegetables", "price": 100},
    {"name": "corn", "category": "vegetables", "price": 40},
    {"name": "peas", "category": "vegetables", "price": 60},
    {"name": "banana leaf", "category": "vegetables", "price": 10},
    {"name": "pumpkin", "category": "vegetables", "price": 50},
    {"name": "lettuce", "category": "vegetables", "price": 60},
]

for p in products:
    image_path = f"products/{p['name'].replace(' ', '_')}.jpg"
    
    # Check if product already exists
    if Product.objects.filter(name=p['name']).exists():
        print(f"{p['name']} already exists. Skipping.")
        continue

    product = Product(
        name=p['name'],
        category=p['category'],
        price=p['price'],
        description=f"Fresh {p['name']} available now!"
    )
    # Set image field
    product.image.name = image_path
    product.save()
    print(f"Added {p['name']} to database.")
