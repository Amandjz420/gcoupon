from datetime import datetime, timedelta
from marshmallow import post_load, pre_load, post_dump
from django.utils.timezone import get_current_timezone

from elapi.base_schema import Schema
from elapi.fields import fields


class CouponSchema(Schema):

    id = fields.Integer()
    name = fields.String(attribute='revised_coupon_name')
    link = fields.String()
    status = fields.String()
    expiry_time = fields.DateTime(attribute='end_date',format='%Y-%m-%d %H:%M:%S')
    description = fields.String()
    published = fields.Boolean()
    merchant = fields.String(attribute='mechant.name')
    categories = fields.Method('get_categories')
    type = fields.Method('get_type')

    def get_categories(self, instance, **kwargs):
        categories = []
        for cat in instance.category.all():
            categories.append(cat.name)
        return categories

    def get_type(self, instance, **kwargs):
        coup_type = []
        for item in instance.type.all():
            coup_type.append(item.name)
        return coup_type


class CategorySchema(Schema):

    id = fields.Integer()
    name = fields.String()