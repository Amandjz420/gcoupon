from django.contrib import admin
from .models import Coupon, Merchant, Type, Category
# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Coupon._meta.fields]


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Merchant._meta.fields]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Type._meta.fields]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]


# Register your models here.
