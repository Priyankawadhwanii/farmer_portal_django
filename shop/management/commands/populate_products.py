import os
import random
from django.core.management.base import BaseCommand
from django.core.files import File
from shop.models import Product
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with sample products'

    def handle(self, *args, **kwargs):
        product_data = [
            # Fruits
            ("Apple", "Fresh red apples", "fruits"),
            ("Banana", "Sweet bananas", "fruits"),
            ("Orange", "Juicy oranges", "fruits"),
            ("Mango", "Ripe mangoes", "fruits"),
            ("Grapes", "Fresh grapes", "fruits"),
            ("Pineapple", "Tropical pineapple", "fruits"),
            ("Papaya", "Healthy papaya", "fruits"),
            ("Strawberry", "Red strawberries", "fruits"),
            ("Watermelon", "Sweet watermelon", "fruits"),
            ("Kiwi", "Fresh kiwi", "fruits"),

            # Vegetables
            ("Carrot", "Organic carrots", "vegetables"),
            ("Tomato", "Fresh tomatoes", "vegetables"),
            ("Potato", "Healthy potatoes", "vegetables"),
            ("Onion", "Fresh onions", "vegetables"),
            ("Cucumber", "Crispy cucumber", "vegetables"),
            ("Spinach", "Green spinach", "vegetables"),
            ("Cauliflower", "Fresh cauliflower", "vegetables"),
            ("Broccoli", "Healthy broccoli", "vegetables"),
            ("Capsicum", "Green capsicum", "vegetables"),
            ("Beetroot", "Fresh beetroot", "vegetables"),

            # Dairy
            ("Milk", "Fresh cow milk", "dairy"),
            ("Paneer", "Homemade paneer", "dairy"),
            ("Curd", "Fresh curd", "dairy"),
            ("Butter", "Organic butter", "dairy"),
            ("Cheese", "Cheddar cheese", "dairy"),
            ("Ghee", "Pure ghee", "dairy"),
            ("Yogurt", "Natural yogurt", "dairy"),
            ("Cream", "Fresh cream", "dairy"),
            ("Buttermilk", "Healthy buttermilk", "dairy"),
            ("Ice Cream", "Vanilla ice cream", "dairy"),
        ]

        media_path = os.path.join(settings.BASE_DIR, "media/products")
        
        for name, desc, category in product_data:
            image_filename = f"{name.lower().replace(' ', '_')}.jpg"
            image_path = os.path.join(media_path, image_filename)

            if not os.path.exists(image_path):
                self.stdout.write(self.style.WARNING(f"Image {image_filename} not found, skipping {name}"))
                continue

            with open(image_path, 'rb') as f:
                product, created = Product.objects.get_or_create(
                    name=name,
                    defaults={
                        "description": desc,
                        "price": round(random.uniform(20, 300), 2),
                        "category": category,
                    }
                )
                product.image.save(image_filename, File(f), save=True)
                product.save()
                self.stdout.write(self.style.SUCCESS(f"Added product: {name}"))
