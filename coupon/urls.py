from django.conf.urls import url

from .views import CouponListApi, CategoryListApi

app_name = 'coupon'
urlpatterns = [
    url(r'^coupon/$', CouponListApi.as_view(), name='couponList'),
    url(r'^category/$', CategoryListApi.as_view(), name='couponList'),
]