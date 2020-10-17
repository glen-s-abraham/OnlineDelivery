from rest_framework import serializers
from UserManagement.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	"""Serializer for User profile"""
	class Meta:
		model=UserProfile
		fields=('id','email','name','mobile','address_l1','address_l2','city','state','password')
		extra_kwargs={
			'password':{
						'write_only':True,
						'style':{'input_type':'password'}
			}
		}
		
	def create(self,validated_data):	
		user=UserProfile.Objects.create_user(
				email=validated_data['email'],
				name=validated_data['name'],
				mobile=validated_data['mobile'],
				address_l1=validated_data['address_l1'],
				address_l2=validated_data['address_l2'],
				city=validated_data['city'],
				state=validated_data['state'],
				password=validated_data['password']
					
				)
			

		return user

