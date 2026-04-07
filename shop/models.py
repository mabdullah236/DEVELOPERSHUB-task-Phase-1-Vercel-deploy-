from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, help_text="e.g. Pakpattan, Lahore, Berlin")
    country = models.CharField(max_length=50, default="Pakistan")
    country_code = models.CharField(max_length=2, default="pk", help_text="2-letter code e.g. pk, us")
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CONDITION_CHOICES = (('Any', 'Any'),('Refurbished', 'Refurbished'),('Brand new', 'Brand new'),('Old items', 'Old items'),)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    features = models.ManyToManyField(Feature, blank=True)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default='Brand new')
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    prev_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="products/")
    description = models.TextField()
    stock = models.IntegerField(default=0)
    sold_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    @property
    def formatted_sold(self):
        if self.sold_count >= 1000000:
            return f"{self.sold_count / 1000000:.1f}M".replace('.0M', 'M')
        elif self.sold_count >= 1000:
            return f"{self.sold_count / 1000:.1f}K".replace('.0K', 'K')
        return str(self.sold_count)

    @property
    def star_rating_classes(self):
        stars = []
        rating_val = float(self.rating)
        for i in range(1, 6):
            if rating_val >= i:
                stars.append('fa-solid fa-star text-warning')
            elif rating_val >= i - 0.5:
                stars.append('fa-solid fa-star-half-stroke text-warning')
            else:
                stars.append('fa-regular fa-star text-muted')
        return stars

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to="products/gallery/")

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    @property
    def total_bill(self):
        return sum(item.subtotal for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def subtotal(self):
        return self.product.new_price * self.quantity

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} saved {self.product.name}"