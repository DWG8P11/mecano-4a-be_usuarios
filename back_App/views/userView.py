from rest_framework                       import status, views
from rest_framework.response              import Response
from back_App.serializers                 import UserSerializer
from back_App.serializers 			      import MiTokenObtainPairSerializer
from rest_framework                       import generics, status
from rest_framework.permissions           import IsAuthenticated
from back_App.models.users                import Usuario
from rest_framework.permissions			  import IsAuthenticated


class UserCreateView(views.APIView):

	def post (self,request,*args,**kwards):
		serializer = UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		tokenData = {"correo":request.data ["correo"],
		"password":request.data["password"]} 
	
		tokenSerializer = MiTokenObtainPairSerializer(data=tokenData)
		tokenSerializer.is_valid(raise_exception=True)
		return Response(tokenSerializer.validated_data,status=status.HTTP_201_CREATED)

class UserDetailView(generics.RetrieveAPIView):

	queryset           = Usuario.objects.all()
	serializer_class   = UserSerializer
	permission_classes = (IsAuthenticated,)

class UserUpdateView(generics.UpdateAPIView):

	queryset           = Usuario.objects.all()
	serializer_class   = UserSerializer
	permission_classes = (IsAuthenticated,)

	def update(self, request, *args, **kwargs):
		return super().update(self, request, *args, **kwargs)

class UserDeleteView(generics.DestroyAPIView):

	queryset           = Usuario.objects.all()
	serializer_class   = UserSerializer
	permission_classes = (IsAuthenticated,)
	
	def delete(self, request, *args, **kwargs):
		return super().destroy(self, request, *args, **kwargs)
	
	

	