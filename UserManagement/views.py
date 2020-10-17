from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from UserManagement.serializer import UserProfileSerializer
from UserManagement.models import UserProfile
from UserManagement.permissions import IsOwnerOrReadOnly

class UserProfileView(viewsets.ModelViewSet):
	permission_classes = [IsOwnerOrReadOnly]
	serializer_class=UserProfileSerializer
	queryset=UserProfile.Objects.all()

	def get_queryset(self):
		user=self.request.user.id
		return UserProfile.Objects.filter(id=user) 