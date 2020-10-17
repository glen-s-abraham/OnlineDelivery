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

