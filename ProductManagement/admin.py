from django.contrib import admin
from ProductManagement import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Category)
