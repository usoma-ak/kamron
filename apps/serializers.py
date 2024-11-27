from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import Product, Category


class CategoryModelSerializer(ModelSerializer):
	product_count = SerializerMethodField()

	class Meta:
		model = Category
		fields = "__all__"

	def get_product_count(self, obj):
		return obj.products.count()


class ProductModelSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

	def to_representation(self, instancex):
		repr = super().to_representation(instance)
		repr['category'] = CategoryModelSerializer(instance.category).data
		return

