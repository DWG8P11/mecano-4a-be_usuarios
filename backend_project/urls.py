"""backend_project URL Configuration
"""
from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView )
from back_App.views.userView        import (UserCreateView, UserDetailView)
from back_App.views.verifyTokenView import VerifyTokenView

urlpatterns = [
    path('admin/',         admin.site.urls),
    path('verifyToken/',   VerifyTokenView.as_view()),
    path('login/',         TokenObtainPairView.as_view()),
    path('refresh/',       TokenRefreshView.as_view()),
    path('user/',          UserCreateView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),

]
