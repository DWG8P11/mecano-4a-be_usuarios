from ..models       import users
from rest_framework import serializers
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = users.Usuario
        # Datos que se podrán recibir al utilizar el serializador para
        # crear un usuario a partir de un JSON
        fields = ['id','self', 'nombre','correo','telefono','pais','departamento','ciudad','usuario', 'contrasena','is_staff']
 
    def create(self, validated_data):
        '''
        Método para crear un Usuario a partir de un JSON
        '''
        
        userInstance = users.Usuario.objects.create_user(**validated_data)
        return userInstance
 
    def to_representation(self, usuario):
        '''
        Método para crear un JSON a partir de un usuario existente
        '''
        user   = usuario.Usuario.objects.get(id = usuario.id)
        return {
            "nombre"       : user.nombre,
            "correo"       : user.email,
            "administrador": user.is_staff
        }

