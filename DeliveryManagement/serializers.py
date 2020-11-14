from rest_framework import serializers
from OrderManagement.models import Order
from UserManagement.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	"""Model serializer for ordered product model"""
	
	class Meta:

		model=UserProfile
		fields=('id','name','mobile','address_l1','address_l2','city')
		read_only_fields = ('id','name','mobile','address_l1','address_l2','city')


class OrderSerializer(serializers.ModelSerializer):
	"""Order serializer"""
	user=UserProfileSerializer(many=False)
	class Meta:
		model=Order
		fields=('id','total_amount','status','user')
		read_only_fields = ('id','total_amount','user')
	
	def create(self,validated_data):
		pass		
	def update(self,instance,validated_data):
		instance.status=validated_data.get('status', instance.status)
		instance.save()
		return instance