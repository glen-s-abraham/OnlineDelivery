from django.urls import path,include
from rest_framework import routers

from ProductManagement import views

router=routers.DefaultRouter()
router.register('List',views.ProductView)
router.register('List/<int:cat>',views.ProductView)


urlpatterns = [
   path('',include(router.urls)),
   


]
