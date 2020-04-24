from celery import task
from .models import Coupon
from datetime import datetime


@task(name='coupon_expiry')
def check_coupons_status():
    coupons = Coupon.objects.all()
    for obj in coupons:

        if datetime.now(obj.end_date.tzinfo) >= obj.end_date or datetime.now(obj.start_date.tzinfo) <= obj.start_date:
            obj.status = 'inactive'
            obj.save()
    print('done')