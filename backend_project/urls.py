"""backend_project URL Configuration
"""
from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import TokenRefreshView
from back_App.views                 import MiTokenObtainPairView
from back_App.views.userView        import (UserCreateView, UserDetailView,UserDeleteView,UserUpdateView)
from back_App.views.verifyTokenView import VerifyTokenView


urlpatterns = [
    path('admin/',           admin.site.urls),
    path('verifyToken/',     VerifyTokenView.as_view()),
    path('login/',           MiTokenObtainPairView.as_view()),
    path('refresh/',         TokenRefreshView.as_view()),
    path('user/',            UserCreateView.as_view()),
    path('user/<int:pk>/',   UserDetailView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()), 
    path('update/<int:pk>/', UserUpdateView.as_view()), 


]
