from django.urls import path,include
from rest_framework import routers

from DeliveryManagement import views

router=routers.DefaultRouter()
router.register('DeliveryList/',views.DeliveryView)




urlpatterns = [
   path('',include(router.urls)),
   


]