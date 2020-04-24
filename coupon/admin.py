from django.contrib import admin
from django.contrib import messages
from datetime import datetime, timedelta
from django.forms import ValidationError as FormValidationError
from django.http import HttpResponseRedirect

from .models import Coupon, Merchant, Type, Category

# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Coupon._meta.fields]
    fields = (
        'coupon_number', 'original_coupon_name', 'revised_coupon_name',
        'merchant', 'category', 'network', 'type', 'rating',
        'start_date', 'end_date', 'description',
    )
    readonly_fields = [
        'original_coupon_name', 'coupon_number', 'status',
        'start_date', 'end_date', 'rating', 'link',
        'category', 'type', 'restriction', 'network', 'merchant',
        'desc_updated', 'code', 'image'
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(CouponAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['description'].widget.attrs['style'] = 'width: 45em;height: 20em;'
        form.base_fields['revised_coupon_name'].widget.attrs['style'] = 'width: 70%;'
        return form

    def save_model(self, request, obj, form, change):
        if datetime.now(obj.modified.tzinfo) >= obj.modified + timedelta(minutes=15) \
            or not obj.desc_updated or request.user.id == obj.desc_updated.id:
            obj.desc_updated = request.user
            super().save_model(request, obj, form, change)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'This Coupon has recently been updated by ' + obj.desc_updated.username +". Try again in 15 mins")

    def response_change(self, request, obj, post_url_continue=None):
        """This makes the response go to the newly created model's change page
        without using reverse"""
        if datetime.now( obj.modified.tzinfo) >= obj.modified + timedelta(minutes=15)\
            or not obj.desc_updated or request.user.id == obj.desc_updated.id:
            return super(CouponAdmin, self).response_change(request, obj)
        else:
            return HttpResponseRedirect(request.path_info)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True
        return super(CouponAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

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
