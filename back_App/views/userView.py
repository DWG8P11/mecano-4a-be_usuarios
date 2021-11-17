from rest_framework import status, views
from rest_framework.response import Response
from back_App.serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
from rest_framework import generics, status
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from back_App.models.users import Usuario


class UserCreateView(views.APIView):

	def post (self,request,*args,**kwards):
		serializer = UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		tokenData = {"usuario":request.data ["usuario"],
		"contrasena":request.data["contrasena"]} 
	
		tokenSerializer =TokenObtainPairSerializer(data=tokenData)
		tokenSerializer.is_valid(raise_exception=True)
		return Response(tokenSerializer.validated_data,status=status.HTTP_201_CREATED)

class UserDetailView(generics.RetrieveAPIView):

	queryset = Usuario.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):

		token = request.META.get('HTTP_AUTHORIZATION')[7:]
		
		tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
		token_valid_data = tokenBackend.decode(token,verify=False)
		
		if token_valid_data['user_id'] != kwargs['id_user_url']:
			stringResponse = {'detail':'Unauthorized Request'}

			return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
		return super().get(request, *args, **kwargs)


