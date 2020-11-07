from rest_framework import viewsets
from rest_framework import generics
from OrderManagement.serializers import OrderSerializer,OrderedProductSerializer
from OrderManagement.models import Order,OrderedProduct



class OrderView(viewsets.ModelViewSet):
	"""Product View"""
	
	serializer_class=OrderSerializer
	model=Order
	queryset=Order.objects.all()

	def get_queryset(self):
		return Order.objects.filter(user=self.request.user)



	
