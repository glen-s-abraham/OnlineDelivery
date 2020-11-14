from rest_framework import viewsets
from DeliveryManagement.serializers import OrderSerializer
from OrderManagement.models import Order
from UserManagement.models import DeliveryStaff
from DeliveryManagement.permissions import IsAdminUser

class DeliveryView(viewsets.ModelViewSet):
	"""Product View"""
	
	serializer_class=OrderSerializer
	permission_classes=[IsAdminUser]
	model=Order
	queryset=Order.objects.all()

	def get_queryset(self):
		staff=None
		try:
			staff=DeliveryStaff.objects.get(staff=self.request.user)
			
		except:
			pass	
			
		if staff:
			return Order.objects.filter(assign_to=staff)	
			
		