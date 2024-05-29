from django.shortcuts import render
from rest_framework import viewsets
from .models import user, CustomUser
from .serializers import UserSignUpSerializer, UserLoginSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):   
    queryset = CustomUser.objects.all()
    serializer_class = UserSignUpSerializer 

    @action(detail=False, methods=['post'])
    def signup(self, request):
        # request.data는 이미 딕셔너리 형태이므로 json.loads가 필요 없습니다.
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "회원가입 실패", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginViewSet(viewsets.ModelViewSet): 
    queryset = user.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        
        if request.data is not None:
            login(request, user)
            return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "로그인 실패"}, status=status.HTTP_400_BAD_REQUEST)


    






