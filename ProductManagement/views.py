from rest_framework import viewsets

from rest_framework import filters

from ProductManagement.serializers import ProductManagementSerializer
from ProductManagement.serializers import CategorySerializer
from ProductManagement.models import Product
from ProductManagement.models import Category
from ProductManagement import permissions


class ProductView(viewsets.ModelViewSet):
	"""Product View"""
	permission_classes = (permissions.IsAdminUser, )
	serializer_class=ProductManagementSerializer
	queryset=Product.objects.all()
	filter_backends = [filters.SearchFilter]
	search_fields = ['title',]
	
    

	def get_queryset(self):
		catid=self.request.query_params.get('cat', None)
		if catid:
			return Product.objects.filter(category=catid)
		return Product.objects.all()

class CategoryView(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAdminUser, )
	serializer_class=CategorySerializer
	queryset=Category.objects.all()
	
	