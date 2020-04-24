import json
import datetime

from django.core.management.base import BaseCommand
from django.utils.timezone import get_current_timezone

from coupon.models import Coupon, Merchant, Type, Category


class Command(BaseCommand):
    help = 'Populate data from json file'

    def add_arguments(self, parser):

        # Optional argument
        parser.add_argument('-p', '--path', type=str, help='populate coupon data', )

    def handle(self, *args, **kwargs):

        prefix = kwargs['path']
        field_values = {}
        try:
            with open((str(prefix))) as data_file:
                data = json.load(data_file)
                for item in data:
                    print(item)
        except Exception as e:
            print(e)
