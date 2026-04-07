from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('products/grid/', views.product_grid, name='product_grid'),
    path('products/list/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail,name='product_detail'),
    path('auth/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('cart/',views.cart,name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('move-to-cart/<int:id>/', views.move_to_cart, name='move_to_cart'),
    path('update-cart/<int:id>/', views.update_cart, name='update_cart'),
    path('add-to-wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('admin-dashboard/add-product/', views.add_product, name='add_product'),
    path('admin-dashboard/add-category-ajax/', views.ajax_add_category, name='add_category_ajax'),
    path('admin-dashboard/add-brand-ajax/', views.ajax_add_brand, name='add_brand_ajax'),
    path('admin-dashboard/add-supplier-ajax/', views.ajax_add_supplier, name='add_supplier_ajax'),
    path('admin-dashboard/add-feature-ajax/', views.ajax_add_feature, name='add_feature_ajax'),
]
