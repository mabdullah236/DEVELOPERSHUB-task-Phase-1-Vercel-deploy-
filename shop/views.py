from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Wishlist
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse # AJAX ke liye naya import
from .forms import ProductForm, CategoryForm, BrandForm, SupplierForm, FeatureForm
from .models import Product, Category, Brand, Supplier, Feature, ProductImage, ProductSpecification

def home(request):
    # Recommended/Featured products
    featured_products = Product.objects.filter(is_featured=True).order_by('?')[:8]
    
    # Sidebar Categories
    categories = Category.objects.all()
    
    # Deals & Offers
    deals = Product.objects.filter(discount_percentage__gt=0).order_by('-discount_percentage')[:5]
    block1_cat = categories[0] if categories.count() > 0 else None
    block1_prods = Product.objects.filter(category=block1_cat).order_by('?')[:8] if block1_cat else []
    block2_cat = categories[1] if categories.count() > 1 else None
    block2_prods = Product.objects.filter(category=block2_cat).order_by('?')[:8] if block2_cat else []

    context = {
        'featured_products': featured_products,
        'categories': categories,
        'deals': deals,
        'block1_cat': block1_cat,
        'block1_prods': block1_prods,
        'block2_cat': block2_cat,
        'block2_prods': block2_prods,
    }
    return render(request, "shop/index.html", context)


def product_grid(request):
    all_products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    features = Feature.objects.all()

    query = request.GET.get('q')
    if query:
        all_products = all_products.filter(name__icontains=query)
        
    selected_category_name = "Store"
    category_id = request.GET.get('category')
    if category_id:
        all_products = all_products.filter(category_id=category_id)
        cat = Category.objects.filter(id=category_id).first()
        if cat:
            selected_category_name = cat.name
        
    brand_ids = request.GET.getlist('brand')
    if brand_ids:
        all_products = all_products.filter(brand_id__in=brand_ids)
        
    feature_ids = request.GET.getlist('feature')
    if feature_ids:
        all_products = all_products.filter(features__id__in=feature_ids).distinct()
        
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        all_products = all_products.filter(price__gte=min_price)
    if max_price:
        all_products = all_products.filter(price__lte=max_price)
        
    condition = request.GET.get('condition')
    if condition and condition != 'Any':
        all_products = all_products.filter(condition=condition)

    total_items = all_products.count()

    paginator = Paginator(all_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'features': features,
        'conditions': ['Refurbished', 'Brand new', 'Old items'],
        'total_items': total_items, 
        'selected_category_name': selected_category_name
    }
    return render(request, 'shop/product_grid.html', context)


def product_list(request):
    all_products = Product.objects.all()
    
    categories = Category.objects.all()
    brands = Brand.objects.all()
    features = Feature.objects.all()

    query = request.GET.get('q')
    if query:
        all_products = all_products.filter(name__icontains=query)
    
    selected_category_name = "Store"
    category_id = request.GET.get('category')
    if category_id:
        all_products = all_products.filter(category_id=category_id)
        cat = Category.objects.filter(id=category_id).first()
        if cat:
            selected_category_name = cat.name
    
    brand_ids = request.GET.getlist('brand')
    if brand_ids:
        all_products = all_products.filter(brand_id__in=brand_ids)
        
    feature_ids = request.GET.getlist('feature')
    if feature_ids:
        all_products = all_products.filter(features__id__in=feature_ids).distinct()
    
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        all_products = all_products.filter(new_price__gte=min_price)
    if max_price:
        all_products = all_products.filter(new_price__lte=max_price)
        
    condition = request.GET.get('condition')
    if condition and condition != 'Any':
        all_products = all_products.filter(condition=condition)

    total_items = all_products.count()

    paginator = Paginator(all_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'features': features,
        'conditions': ['Refurbished', 'Brand new', 'Old items'],
        'total_items': total_items, 
        'selected_category_name': selected_category_name,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, id):
    single_product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=single_product.category).exclude(id=single_product.id)[:4]
    may_like = Product.objects.all().exclude(id=single_product.id)[:5]
    context = {
        'product': single_product,
        'like': may_like,
        'related_products': related_products
    }
    return render(request, 'shop/product_detail.html', context)

@login_required(login_url='login_view')
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    saved_items = request.user.wishlist.all()
    
    # Bill Calculation
    subtotal = 0
    total_discount = 0
    total_tax = 0
    
    for item in cart_items:
        item_sub = item.product.new_price * item.quantity
        subtotal += item_sub
        total_discount += (item_sub * item.product.discount_percentage) / 100
        total_tax += (item_sub * item.product.tax_percentage) / 100
        
    total = float(subtotal) - float(total_discount) + float(total_tax)
    
    context = {
        'cart_items': cart_items,
        'saved_items': saved_items,
        'subtotal': subtotal,
        'tax': total_tax,
        'discount': total_discount,
        'total': total,
        'total_qty': sum(item.quantity for item in cart_items),
    }
    return render(request, 'shop/cart.html', context)

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Password Match Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match. Please try again.")
            return redirect('signup_view')

        # Duplicate Username Check
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken. Please choose another one.")
            return redirect('signup_view')

        # Duplicate Email Check
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered. Please log in instead.")
            return redirect('signup_view')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "Your account has been created successfully! You can now log in.")
        return redirect('login_view')

    return render(request, 'shop/auth.html')

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        
        user = authenticate(request, username=user_name, password=pass_word)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('signup_view')

    return render(request, 'shop/auth.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login_view')
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if CartItem.objects.filter(cart=cart, product=product).exists():
        messages.warning(request, f"'{product.name}' is already in your cart.")
    elif Wishlist.objects.filter(user=request.user, product=product).exists():
        messages.warning(request, f"'{product.name}' is already in your wishlist. Please move it to your cart from there.")
    else:
        CartItem.objects.create(cart=cart, product=product, quantity=1)
        messages.success(request, f"'{product.name}' has been successfully added to your cart.")
        
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required(login_url='login_view')
def remove_from_cart(request, id):
    item = get_object_or_404(CartItem, id=id, cart__user=request.user)
    item_name = item.product.name
    item.delete()
    messages.error(request, f"'{item_name}' removed from cart.") 
    return redirect('cart')

@login_required(login_url='login_view')
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if CartItem.objects.filter(cart=cart, product=product).exists():
        messages.warning(request, f"'{product.name}' is already in your cart. Please remove it from the cart to save it for later.")
    elif Wishlist.objects.filter(user=request.user, product=product).exists():
        messages.warning(request, f"'{product.name}' is already in your wishlist.")
    else:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, f"'{product.name}' has been successfully saved for later.")
        
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required(login_url='login_view')
def remove_from_wishlist(request, id):
    Wishlist.objects.filter(id=id, user=request.user).delete()
    return redirect('cart')

@login_required(login_url='login_view')
def move_to_cart(request, id):
    wishlist_item = get_object_or_404(Wishlist, id=id, user=request.user)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=wishlist_item.product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    wishlist_item.delete()
    
    messages.success(request, f"{wishlist_item.product.name} moved to cart!")
    return redirect('cart')

@login_required(login_url='login_view')
def update_cart(request, id):
    qty = int(request.GET.get('qty', 1))
    cart_item = get_object_or_404(CartItem, id=id, cart__user=request.user)
    
    # Stock Protection Logic
    if qty > cart_item.product.stock:
        messages.error(request, f"Sorry, only {cart_item.product.stock} items available in stock!")
        cart_item.quantity = cart_item.product.stock
    else:
        cart_item.quantity = qty
        
    cart_item.save()
    return redirect('cart')

@staff_member_required(login_url='login_view')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['name']
            if Product.objects.filter(name__iexact=product_name).exists():
                messages.error(request, f"Product '{product_name}' already exists in the store!")
                return redirect('add_product')
            
            product = form.save()
            
            gallery_images = request.FILES.getlist('gallery_images') 
            for img in gallery_images:
                ProductImage.objects.create(product=product, image=img)
                
            spec_keys = request.POST.getlist('spec_keys[]')
            spec_values = request.POST.getlist('spec_values[]')
            
            for key, value in zip(spec_keys, spec_values):
                if key.strip() and value.strip(): 
                    ProductSpecification.objects.create(product=product, key=key, value=value)

            messages.success(request, f"'{product.name}' along with gallery and specs added successfully!")
            return redirect('add_product')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'cat_form': CategoryForm(),
        'brand_form': BrandForm(),
        'supplier_form': SupplierForm(),
        'feature_form': FeatureForm()
    }
    return render(request, 'shop/add_product.html', context)

@staff_member_required(login_url='login_view')
def ajax_add_category(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        if name:
            obj, created = Category.objects.get_or_create(name=name)
            if created:
                return JsonResponse({'status': 'success', 'id': obj.id, 'name': obj.name})
            return JsonResponse({'status': 'error', 'message': 'This category already exists.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

@staff_member_required(login_url='login_view')
def ajax_add_brand(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        if name:
            obj, created = Brand.objects.get_or_create(name=name)
            if created:
                return JsonResponse({'status': 'success', 'id': obj.id, 'name': obj.name})
            return JsonResponse({'status': 'error', 'message': 'This brand already exists.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

@staff_member_required(login_url='login_view')
def ajax_add_feature(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        if name:
            obj, created = Feature.objects.get_or_create(name=name)
            if created:
                return JsonResponse({'status': 'success', 'id': obj.id, 'name': obj.name})
            return JsonResponse({'status': 'error', 'message': 'This feature already exists.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

@staff_member_required(login_url='login_view')
def ajax_add_supplier(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        location = request.POST.get('location')
        country_code = request.POST.get('country_code', 'pk')
        is_verified_val = request.POST.get('is_verified')
        is_verified = is_verified_val in ['true', 'True', 'on', '1']

        if name:
            obj, created = Supplier.objects.get_or_create(name=name, defaults={'location': location, 'country_code': country_code, 'is_verified': is_verified})
            if created:
                return JsonResponse({'status': 'success', 'id': obj.id, 'name': obj.name})
            return JsonResponse({'status': 'error', 'message': 'This supplier already exists.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})