from rest_framework_simplejwt.views import TokenObtainPairView
from back_App.serializers import MiTokenObtainPairSerializer

class MiTokenObtainPairView(TokenObtainPairView):
    serializer_class = MiTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()