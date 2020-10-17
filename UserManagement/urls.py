from django.urls import path,include
from rest_framework import routers
from UserManagement import views

router=routers.DefaultRouter()
router.register('Profiles',views.UserProfileView)


urlpatterns = [
   path('',include(router.urls))

]
