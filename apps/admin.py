from django.contrib.admin import register, ModelAdmin
from django.db import connections

from apps.models import Product, Category


# @register(Product)
# class ProductModelAdmin(ModelAdmin):
# 	# list_display = 'name',  # 'data__color'
# 	# search_fields = 'data__size', 'data__color'
# 	pass
# # @admin.display(description='Rangi')
# # def data__color(self, obj: Event):
# # 	return obj.data['color']
#
#


@register(Category)
class CategoryModelAdmin(ModelAdmin):
	pass


@register(Product)
class CategoryModelAdmin(ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.save()

		# with connections['second_db'].cursor() as cursor:
		# 	cursor.execute("INSERT INTO apps_product(title, price) VALUES (%s, %s);", [obj.name, obj.price])

