from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
import random
import re

# Create your views here.
from api.user.models import User
from api.user.serializers import UserSerializer


def generate_session_token(length=32):
    # Generates a session token with length of 128bits
    list_options = [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)]
    return ''.join(random.SystemRandom().choice(list_options) for _ in range(length))


@csrf_exempt
def sign_in(request):
    if not request.method == 'POST':
        return JsonResponse({"error": "Send a POST request with valid parameters"})

    username = request.POST['email']
    password = request.POST['password']

    # Email Validation
    if not re.math(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', username):
        return JsonResponse({"error": "Enter a valid email"})

    # Password Validation
    if len(password) < 6:
        return JsonResponse({'error': "Password must be at least 6 characters"})

    UserModel = get_user_model()

    try:
        user = UserModel.object.get(email=username)

        if user.check_password(password):
            user_dict = UserModel.object \
                .filter(email=username) \
                .values() \
                .first()
            user_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': 'Previous session exists'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({"token": token, 'user': user_dict})
        return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


def sign_out(request):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.object.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({"error": "Invalid user ID"})
    return JsonResponse({'success': "Logout success"})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    query_set = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
