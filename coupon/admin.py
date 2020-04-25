from django.contrib import admin
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils.html import format_html
from django.http import HttpResponseRedirect

from .models import Coupon, Merchant, Type, Category


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_number', 'revised_coupon_name', 'status',
                    'merchant', 'published_entry', 'desc_updated',
                    'start_date', 'end_date', 'description', 'view_categories',
                    ]
    fields = (
        'coupon_number', 'original_coupon_name', 'revised_coupon_name',
        'merchant', 'status', 'published', 'category', 'network', 'type',
        'start_date', 'end_date', 'description', 'desc_updated', 'modified',
        'rating',
    )
    readonly_fields = [
        'original_coupon_name', 'coupon_number', 'status',
        'start_date', 'end_date', 'rating', 'link',
        'category', 'type', 'restriction', 'network', 'merchant',
        'desc_updated', 'code', 'image', 'modified',
    ]

    def published_entry(self, obj):
        if obj.published:
            return format_html("<div style='background:#4CAF50;color:white;text-align:center;border-radius:3px;padding:1px'>Published</div>", obj.id)
        return format_html("<a href='/admin/coupon/coupon/{0}' style='background:#447e9b;color: white;padding: 5px;border-radius: 3px;'>Start Writing</a>", obj.id)


    def view_categories(self, obj):
        return list(obj.category.all())

    def get_form(self, request, obj=None, **kwargs):
        form = super(CouponAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['description'].widget.attrs['style'] = 'width: 45em;height: 20em;'
        form.base_fields['revised_coupon_name'].widget.attrs['style'] = 'width: 70%;'
        return form

    def save_model(self, request, obj, form, change):
        if datetime.now(obj.modified.tzinfo) >= obj.modified + timedelta(minutes=15) \
            or not obj.desc_updated or request.user.id == obj.desc_updated.id:
            obj.desc_updated = request.user
            if request.POST['_continue'] is 'Save':
                obj.published = True
            super().save_model(request, obj, form, change)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'This Coupon has recently been updated by ' + obj.desc_updated.username +". Try again in 15 mins")

    def response_change(self, request, obj, post_url_continue=None):
        """This makes the response go to the newly created model's change page
        without using reverse"""
        if datetime.now(obj.modified.tzinfo) >= obj.modified + timedelta(minutes=15)\
            or not obj.desc_updated or request.user.id == obj.desc_updated.id:
            return super(CouponAdmin, self).response_change(request, obj)
        else:
            return HttpResponseRedirect(request.path_info)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if object_id:
            extra_context = extra_context or {}
            extra_context['show_save_and_add_another'] = False
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
