from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MiTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user)
        token['es_administrador'] = user.is_staff
        token['usuario'] = user.usuario
        return token