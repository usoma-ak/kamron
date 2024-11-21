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
from django.db.models import Model, CharField, IntegerField, PositiveIntegerField, ForeignKey, CASCADE


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
#

class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    description = CharField(max_length=255)
    # user = ForeignKey('apps.User', CASCADE, related_name='user')
    category = ForeignKey('apps.Category', CASCADE, related_name='products')

    def __str__(self):
        return self.name
