from django.db import models
from UserManagement.models import UserProfile,DeliveryStaff
from ProductManagement.models import Product
from django.utils.timezone import now

class Order(models.Model):
	"""Model to store order details"""
	STATUS=(
		('pl','PLACED'),
		('pr','PROCESSINGS'),
		('od','OUTFORDELIVERY'),
		('dr','DELIVERED'),
	)
	user=models.ForeignKey(UserProfile,related_name='user',on_delete=models.CASCADE,blank=True,null=True)
	date=models.DateTimeField(default=now)
	total_amount=models.DecimalField(max_digits=5,decimal_places=2)
	status=models.CharField(max_length=50,choices=STATUS,default='pl')
	assign_to=models.ForeignKey(DeliveryStaff,on_delete=models.CASCADE,blank=True,null=True)
	def __str__(self):
		return str(self.id)

	

class OrderedProduct(models.Model):
	"""Model to store order details"""	
	order=models.ForeignKey(Order,related_name='orders',on_delete=models.CASCADE,blank=True,null=True)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	qty=models.DecimalField(max_digits=5,decimal_places=2)
	price=models.DecimalField(max_digits=5,decimal_places=2)
	def __str__(self):
		return str(self.order.id)

	

