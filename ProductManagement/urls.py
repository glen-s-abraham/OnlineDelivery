from django.urls import path,include
from rest_framework import routers
from ProductManagement import views

router=routers.DefaultRouter()
router.register('ProductList',views.ProductView)
router.register('ProductList/<int:cat>',views.ProductView)
router.register('CategoryList/',views.CategoryView)


urlpatterns = [
   path('',include(router.urls)),
   


]
