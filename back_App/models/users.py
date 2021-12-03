from django.db                     import models
from django.contrib.auth.models    import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers   import make_password
from django.core.validators        import MinLengthValidator, MinValueValidator

class UserManager(BaseUserManager):
    '''
    Esta es la clase creada para la gestión de los usuarios

    '''
    
    def create_user(self, nombre,correo,telefono, usuario, password, is_staff = False, pais = None, departamento = None, ciudad = None): 
        # Los argumentos son todos los datos que queremos ingrese el usuario al registrarse
        """
        Creación de un nuevo usuario
        """
        if is_staff:
        # is_staff será el atributo que indicará si el usuario es o no admin, y en ese caso
        # utilizamos el método .create_superuser que tiene ese propósito
            #No se incluye contrasena para posteriormente encriptarla
            return self.create_superuser(nombre = nombre, correo=correo,telefono=telefono,pais=pais,departamento=departamento,ciudad= ciudad,usuario=usuario,password=password)
        usuarioM                = self.model()
        usuarioM.correo         = self.normalize_email(correo)
        usuarioM.nombre         = nombre
        usuarioM.telefono       = telefono
        usuarioM.pais           = pais
        usuarioM.departamento   = departamento
        usuarioM.ciudad         = ciudad
        usuarioM.usuario        = usuario

        # Agregar contrasena a la info del usuario, encriptándola
        
        sal = 'condimento'
        usuarioM.password = make_password(password, sal)
        # Guardar en base de datos
        usuarioM.save(using = self._db)
        return usuarioM
 
    def create_superuser(self, nombre,correo,telefono, usuario, password, pais = None, departamento = None, ciudad = None):
        '''
        Método que se llamará cuando se quiera crear un usuario administrador de la App
        '''
        # Crear un usuario comun y corriente
        usuarioM          = self.create_user(
            correo       = correo, 
            nombre       = nombre,
            telefono     = telefono,
            pais         = pais,
            departamento = departamento,
            ciudad       = ciudad,
            usuario      = usuario,
            password     = password,
        )
 
        # Cambiar a True la propiedad de que es admin
        usuarioM.is_staff = True
       
        # Guardar en base de datos
        usuarioM.save(using = self._db)
 
        return usuario
 
class Usuario(AbstractBaseUser):
    id           = models.BigAutoField    (primary_key = True)
    nombre       = models.CharField       (verbose_name = 'Nombre completo', max_length = 100, blank = False, validators=[MinLengthValidator(4)])
    correo       = models.EmailField      (verbose_name = "Correo electrónico", max_length = 100, unique = True, blank = False, validators=[MinLengthValidator(4)])
    telefono     = models.BigIntegerField (verbose_name = "Teléfono de contacto",null=True, blank=False,validators=[MinValueValidator(0)])
    pais         = models.CharField       (verbose_name = 'País', max_length = 100, null = True)
    departamento = models.CharField       (verbose_name = 'Departamento o Estado', max_length = 100, null = True)
    ciudad       = models.CharField       (verbose_name = 'Ciudad', max_length = 100, null = True)
    password     = models.CharField       (verbose_name = "Contraseña", max_length = 256, blank = False, validators=[MinLengthValidator(6)])
    usuario      = models.CharField       (verbose_name = 'Usuario', max_length = 100, unique = True, blank = False, validators=[MinLengthValidator(4)])
    
    # Propiedad para saber si el usuario va a ser administrador de la aplicacion
    is_staff = models.BooleanField(verbose_name = "Es Administrador", default = False)
 
    objects = UserManager()
 
    # Atributo que indica el campo que se usará para identificación del usuario
    USERNAME_FIELD = 'correo'
   
    # Estos son los atributos los pedirá django al momento de decirle createsuperuser
    REQUIRED_FIELDS = ['nombre', 'usuario']
 
    


   