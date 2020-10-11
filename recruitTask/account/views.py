from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User


class LoginView(views.APIView):
    def post(self, request):
        user = authenticate(request=request, username=request.data.get("username"), password=request.data.get("password"))
        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        response = Response(UserSerializer(user).data)
        response.set_cookie('username', user.get_username())
        return response

class LogoutView(views.APIView):
    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
