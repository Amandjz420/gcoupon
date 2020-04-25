from rest_framework import pagination
from django.db.models import Q

from .schema import CouponSchema, CategorySchema
from .models import Coupon, Category
from elapi.base_views import ListView


class CouponPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 30


class CouponListApi(ListView):
    schema_class = CouponSchema
    pagination_class = CouponPagination

    def get_queryset(self):
        return Coupon.objects.prefetch_related('merchant', 'category', 'type')\
            .all().exclude(status='inactive').exclude(published=False)

    def process_list_queryset(self, qs):
        if self.request.GET.get('filter', None):
            words = self.request.GET['filter'].replace('_', ' ').split(',')

            query_filter = Q(category__name__icontains=words[0])
            query_filter = query_filter | Q(merchant__name__icontains=words[0])
            query_filter = query_filter | Q(type__name__icontains=words[0])
            query_filter = query_filter | Q(revised_coupon_name__icontains=words[0])
            for word in words[1:]:
                query_filter = query_filter | Q(category__name__icontains=word)
                query_filter = query_filter | Q(merchant__name__icontains=word)
                query_filter = query_filter | Q(type__name__icontains=word)
                query_filter = query_filter | Q(revised_coupon_name__icontains=word)

            qs = qs.filter(query_filter).distinct()

        return qs

class CategoryListApi(ListView):
    schema_class = CategorySchema
    pagination_class = CouponPagination

    def get_queryset(self):
        return Category.objects.filter(parent_category=0)
