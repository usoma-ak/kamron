# import uuid
#
# from django.db.models import Model, CharField, ForeignKey, CASCADE, UUIDField, DateTimeField, SlugField
# from django.template.defaultfilters import slugify
# from django.utils import timezone
# from django_jsonform.models.fields import JSONField
#
#
# # class User(AbstractUser):
# # 	def save(self, *args, **kwargs):
# # 		if 'botir' in self.username.lower():
# # 			raise ValidationError('ATMEN!!!!!')
# # 		super().save(*args, **kwargs)
#
# class Category(Model):
# 	name = CharField(max_length=255)
# 	uuid = UUIDField(default=uuid.uuid4, unique=True)
# 	slug = SlugField(unique=True)
#
# 	def save(self, *args, **kwargs):
# 		self.slug = slugify(self.name)
# 		super().save(*args,**kwargs)
#
#
# class Product(Model):
# 	# ITEMS_SCHEMA = {
# 	# 	'type': 'dict',
# 	# 	'keys': {
# 	# 		'size': {
# 	# 			'type': 'number',
# 	# 		},
# 	# 		'color': {
# 	# 			'type': 'string',
# 	# 		},
# 	# 		'storage': {
# 	# 			'type': 'string',
# 	# 		}
# 	# 	},
# 	# 	'required': ['size', 'color']
# 	# }
# 	name = CharField(max_length=255)
# 	# data = JSONField(schema=ITEMS_SCHEMA, blank=True, null=True)
# 	# uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	category1 = ForeignKey('apps.Category', CASCADE, related_name="categories")
# 	category2 = ForeignKey('apps.Category', CASCADE, to_field="slug", related_name="product_slug")
# 	category3 = ForeignKey('apps.Category', CASCADE, to_field="uuid", related_name="product_uuid")
# 	# event_time = DateTimeField()
#
# 	def __str__(self):
# 		return self.name
# from django.db.models import Model, IntegerField
# import calendar
#
#
# class Month(Model):
# 	moth = IntegerField(choices=enumerate(list(calendar.month_name)[1:], start=1))
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, IntegerField, PositiveIntegerField, ForeignKey, CASCADE, BooleanField, \
    Manager, QuerySet


# from django.db.models import Model, CharField
# from django.forms import TimeField
#
#
# class Event(Model):
#     name = CharField(max_length=255)
#     event_time = TimeField()
# class User(AbstractUser):
#
#     def save(self, *args, **kwargs):
#         if 'botir' in self.username.lower():
#             raise ValidationError('Username atmen!')
#
#         super().save(*args, **kwargs)


# class ProductManager(Manager):
#     def top_product(self):
#         return self.filter(is_premium=True, price__gt=15000)
#
#     def __str__(self):
#         return self.name


# class ProductQuerySet(QuerySet):
#     def between_price(self, min_price, max_price):
#         return self.filter(price__gte=min_price, price__lte=max_price)
#
#     def cheap(self):
#         return self.filter(is_premium=False)
#
#
# class ProductManager(Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model, using=self._db)
#
#     def between_price(self, min_price, max_price):
#         return self.get_queryset().between_price(min_price, max_price)
#
#     def cheap(self):
#         return self.get_queryset().cheap()


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    last_price = PositiveIntegerField()
    description = CharField(max_length=255)
    # is_premium = BooleanField(db_default=False)
    # is_deleted = BooleanField(db_default=False)
    # user = ForeignKey('apps.User', CASCADE, related_name='user')
    # objects = ProductManager()
    category = ForeignKey('apps.Category', CASCADE, related_name='products')

    def __str__(self):
        return self.name
