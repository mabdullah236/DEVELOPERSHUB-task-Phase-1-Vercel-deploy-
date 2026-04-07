from .models import Category
from .models import Cart

def global_categories(request):
    categories = Category.objects.all()
    return {'all_categories': categories}

def cart_status(request):
    total_items_in_cart = 0
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        total_items_in_cart = sum(item.quantity for item in cart.items.all())
        
    return {'cart_item_count': total_items_in_cart}