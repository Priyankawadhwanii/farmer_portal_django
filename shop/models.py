from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('fruits', 'Fruits'),
    ('vegetables', 'Vegetables'),
    ('dairy', 'Dairy'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')

    farmer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name
