from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from UserManagement.serializer import UserProfileSerializer
from UserManagement.models import UserProfile
from UserManagement.permissions import IsOwnerOrReadOnly

class UserProfileView(viewsets.ModelViewSet):
	authentication_classes = (TokenAuthentication,)
	permission_classes = [IsOwnerOrReadOnly]
	serializer_class=UserProfileSerializer
	queryset=UserProfile.Objects.all()

	def get_queryset(self):
		user=self.request.user.id
		return UserProfile.Objects.filter(id=user) 

class UserLoginView(ObtainAuthToken):
	"""Login for users to obtain token"""
	renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES	

class UserLogoutView(APIView):
	"""Logout Users"""

	def get(self,request,format=None):
		request.user.auth_token.delete()
		return Response(status=status.HTTP_200_OK)




