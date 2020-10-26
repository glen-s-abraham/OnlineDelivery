from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=255)
	def __str__(self):
		return self.name


class Product(models.Model):
	title=models.CharField(max_length=255)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	qty=models.DecimalField(max_digits=5,decimal_places=2)
	price=models.DecimalField(max_digits=5,decimal_places=2)
	image=models.FileField(upload_to='Products/')
	def __str__(self):
		return self.title


