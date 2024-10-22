from django.core.management.base import BaseCommand
from django.conf import settings
import requests

from myapi.models import Category, Products

class Command(BaseCommand):
    help = 'load data from excel'

    def handle(self, *args, **options):
        excel_file = 'รายจ่าย2.xlsx' 
        url = 'https://fakestoreapi.com/products?limit=5'
        r = requests.get(url)
        products = r.json()
        for p in range(len(products)):
            data  = products[p]
            category, created = Category.objects.get_or_create(name=data['category'])
            product_name = data['title']
            price = data['price']
            description = data['description']
            rating = data['rating']    
            rate = rating['rate']  
            count = rating['count']

            print(data)
            print('------------------------')
            product = Products.objects.create(
                name=product_name,
                price=price,
                description=description,
                category=category,  
                rating=rate,
                rating_count=count
        )

