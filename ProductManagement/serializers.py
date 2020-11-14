from rest_framework import serializers
from ProductManagement.models import Product
from ProductManagement.models import Category

class ProductManagementSerializer(serializers.ModelSerializer):
	"""Model serializer for product model"""
	class Meta:
		model=Product
		fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
	"""Model serializer for product model"""
	class Meta:
		model=Category
		fields='__all__'