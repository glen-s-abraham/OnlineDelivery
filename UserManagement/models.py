from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
	"""Manager class for user profile"""
	def create_user(self,email,name,mobile,address_l1="None",address_l2="None",city="None",state="None",password=None):
		if not email:
			raise ValueError("User must have email")
		email=self.normalize_email(email)
		user=self.model(email=email,name=name,mobile=mobile,address_l1=address_l1,address_l2=address_l2,city=city,state=state)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_superuser(self,email,name,mobile,password):
		user=self.create_user(email=email,name=name,mobile=mobile,password=password)
		user.is_superuser=True
		user.is_staff=True
		user.save(using=self._db)
		return user	

class UserProfile(AbstractBaseUser,PermissionsMixin):
	"""Model for the user profile class"""
	email=models.EmailField(max_length=255,unique=True)
	name=models.CharField(max_length=255)
	mobile=models.CharField(max_length=13)
	address_l1=models.CharField(max_length=255,default=None,blank=True)
	address_l2=models.CharField(max_length=255,default=None,blank=True)
	city=models.CharField(max_length=255,default=None,blank=True)
	state=models.CharField(max_length=255,default=None,blank=True)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)
	Objects=UserProfileManager()
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['name','mobile']

class DeliveryStaff(models.Model):
	"""Details of delivery staff"""
	staff=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)	

