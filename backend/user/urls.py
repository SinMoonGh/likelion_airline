from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet, UserLoginViewSet



router = DefaultRouter()
router.register(r'signup', UserViewSet, basename='signup') 
router.register(r'login', UserLoginViewSet, basename='login')  

urlpatterns = [
    path('', include(router.urls)),
]
