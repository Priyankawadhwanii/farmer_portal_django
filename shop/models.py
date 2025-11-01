from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('fruits', 'Fruits'),
    ('vegetables', 'Vegetables'),
    ('dairy', 'Dairy'),
    ('Grains', 'Grains'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='fruits')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('consumer', 'Consumer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
