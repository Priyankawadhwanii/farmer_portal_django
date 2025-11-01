# shop/context_processors.py
from .models import Profile

def cart_and_role(request):
    """Context processor to add cart count and user role to all templates"""
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values()) if cart else 0
    
    user_role = None
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            user_role = profile.role
        except Profile.DoesNotExist:
            user_role = None
    
    return {
        'cart_count': cart_count,
        'user_role': user_role,
    }