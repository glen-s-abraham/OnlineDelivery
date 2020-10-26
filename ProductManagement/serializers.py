from rest_framework import serializers
from ProductManagement.models import Product

class ProductManagementSerializer(serializers.ModelSerializer):
	"""Model serializer for product model"""
	class Meta:
		model=Product
		fields='__all__'
