
from rest_framework.response import Response
from rest_framework import viewsets

from users.serializers import UserSerializer

from users.serializers import UserCreationsSerializer

from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserCreationsSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data)
        return Response(serializer.errors)