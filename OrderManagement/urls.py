from django.urls import path,include
from rest_framework import routers

from OrderManagement import views

router=routers.DefaultRouter()
router.register('OrderList',views.OrderView)




urlpatterns = [
   path('',include(router.urls)),
   


]
