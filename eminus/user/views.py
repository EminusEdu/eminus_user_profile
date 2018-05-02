from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import MyUser
from .serializers import MyUserSerializer

# Create your views here.
class MyUserView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    http_method_names = ['get', 'post']
    # def get(self, request):
    #     users = MyUser.objects.all()
    #     serializer = MyUserSerializer(users)
    #     return Response(serializer.data)
