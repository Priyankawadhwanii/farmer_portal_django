# shop/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Profile

# Base form class with consistent styling
class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-green-500'
            })

# Farmer Registration Form
class FarmerRegisterForm(StyledFormMixin, UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create or update profile
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={'role': 'farmer'}
            )
            if not created:
                profile.role = 'farmer'
                profile.save()
        return user

# Consumer Registration Form  
class ConsumerRegisterForm(StyledFormMixin, UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create or update profile
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={'role': 'consumer'}
            )
            if not created:
                profile.role = 'consumer'
                profile.save()
        return user

# Product Form
class ProductForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add specific styling for select and textarea
        self.fields['category'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-green-500'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-green-500'
        })
