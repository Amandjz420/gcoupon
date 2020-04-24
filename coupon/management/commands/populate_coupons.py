import json
import datetime

from django.core.management.base import BaseCommand

from coupon.models import Coupon, Merchant, Type, Category


class Command(BaseCommand):
    help = 'Populate data from json file'

    def add_arguments(self, parser):

        # Optional argument
        parser.add_argument('-p', '--path', type=str, help='populate coupon data', )

    def handle(self, *args, **kwargs):

        prefix = kwargs['path']
        try:
            with open((str(prefix))) as data_file:
                file = json.load(data_file)
                for index, item in enumerate(file):
                    # merchant creation
                    merchant_data = {
                        "parent_merchant": item['nMasterMerchantID'],
                        "name": item['cMerchant'],
                    }
                    merchant_obj, created = Merchant.objects.\
                        get_or_create(merchant_number=item['nMerchantID'],
                                      defaults=merchant_data)

                    # for categories
                    categories_to_be_added = []
                    if(type(item['aCategoriesV2']) == list):
                        for cat in item['aCategoriesV2']:
                            cat_data = {
                                "parent_category": cat['nParentID'],
                                "cat_number": cat['nCategoryID'],
                            }
                            category_obj, created = Category.objects.get_or_create(
                                name=cat['cName'],
                                defaults=cat_data)
                            categories_to_be_added.append(category_obj)

                    # for types
                    types_to_be_added = []
                    if(type(item['aTypes']) == list):
                        for coup_type in item['aTypes']:
                            type_obj, created = Type.objects. \
                                get_or_create(name=coup_type)

                            types_to_be_added.append(type_obj)

                    coupon_data = {
                        "start_date": datetime.datetime.fromisoformat(item['dtStartDate']),
                        "end_date": datetime.datetime.fromisoformat(item['dtEndDate']),
                        "original_coupon_name": item['cLabel'],
                        "coupon_number": item['nCouponID'],
                        "status": item['cStatus'],
                        "rating": float(item['fRating']),
                        "link": item['cDirectURL'],
                        "restriction": item['cRestrictions'],
                        "network": item['cNetwork'],
                        "code": item['cCode'],
                        "image": item['cImage'],
                        "merchant": merchant_obj,
                    }
                    coupon_obj, creat = Coupon.objects.get_or_create(
                        coupon_number=item['nCouponID'],
                        defaults=coupon_data
                    )
                    coupon_obj.category.add(*categories_to_be_added)
                    coupon_obj.type.add(*types_to_be_added)
                    coupon_obj.save()
        except Exception as e:
            print(e)
