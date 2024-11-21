import datetime
import os
import django
from django.db.models import F, Count
from django.db.models.functions import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Category, Product

# s = input("kiriting>>>: ").strip()

# category = Category.objects.filter(name__icontains='texnika').values_list('name', flat=True)
# product = Product.objects.filter(name__icontains='texnika').values_list('name', flat=True)
#
# t = category.union(product)
#
# print(tuple(t))
#
#
# result = tuple(Category.objects.filter(name__icontains=s).values_list('name', flat=True)
#                .union(Product.objects.filter(name__icontains=s).values_list('name', flat=True)))
# print(result)

# from django.db.models import F, Subquery, Min
#
# Product.objects.update(price=F('price') + Subquery(Product.objects.aggregate(min_price=Min('price'))['min_price']))

# result = Product.objects.values(c_name=F('category__name'))
# for i in result:
# 	print(i)


# from django.db.models import Sum
#
# result = Product.objects.values('category__name', 'name').annotate(count=Count('id'),_price=Sum('price'))
#
# for i in result:
#     print(f"Categoryiasi: {i['category__name']}, Soni: {i['count']}, Nomi: {i['name']}, Narxi: {i['_price']}")


from datetime import datetime

# users = User.objects.filter(date_joined__year=2020)

# products = Product.objects.filter(price__range=(2000, 3500), description__isnull=False, name__icontains='a')
#
# for product in products:
# 	print(f"nomi: {product.name}, narxi: {product.price}, description: {product.description}")
