from django.contrib.admin import register, ModelAdmin

from apps.models import Category, Product


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
	pass

