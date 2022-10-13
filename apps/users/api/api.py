from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

""" class UserAPIView(APIView):
    
    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return Response(user_serializer.data) """

@api_view(['GET', 'POST'])
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return Response(user_serializer.data)
    elif request.method == 'POST':
        print(request.data)
        return