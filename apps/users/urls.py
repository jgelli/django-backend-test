from django.urls import path
from .views import UserCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


app_name = 'users'

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh', TokenRefreshView.as_view(), name='login_refresh'),

]