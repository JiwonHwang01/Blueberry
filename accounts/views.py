from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.middleware.csrf import get_token
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def get_csrf_token(request):
    csrf_token = get_token(request)
    print(csrf_token)
    return JsonResponse({'csrfToken': csrf_token})


from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        user_data = {
            "username": user.username,
            "email": user.email
        }
        print("asdasdasd")
        return JsonResponse({'success': True, 'user': user_data})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=json.loads(request.body))
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user_data = {
                "username": user.username,
                "email": user.email
            }
            return JsonResponse({'success': True, 'user': user_data})  # 메인 페이지로 리디렉션
        else:
            print("Error",form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # 메인 페이지로 리디렉션

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({
        'pk': user.pk,
        'email': user.email,
        'username': user.username,
    })