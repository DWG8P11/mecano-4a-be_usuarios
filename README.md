# Aplicación: La Nebulosa de Qwerty - Backend Gestión de Usuarios

**La Nebulosa de Qwerty** es una aplicación para aprender mecanografía de forma gradual, utilizando como material de aprendizaje y de motivación textos sobre la gran variedad de cuerpos celestes.

Este repositorio corresponde al módulo de backend de _Gestión de Usuarios_ de esta aplicación, desarrollada como proyecto del Ciclo 4 del programa de formación MisiónTIC 2022 Cohorte 2021, por el Equipo 8 del Grupo 11 de Desarrollo Web.

Se hace uso del framework de Python Django para el desarrollo de este módulo, el cual posee una RESTful web API que permite la solicitud de realización operaciones a la aplicación a través de peticiones HTTP que tengan cuerpos en formato JSON.

## Software Necesario

Se requiere de Python 3.9 y un servidor del motor de bases de datos PostgreSQL.

## Instrucciones de instalación

0.  Abrir un shell de línea de comandos y ubicar su directorio en la raíz de este repositorio.

1. Instalar las librerías de Python requeridas: en la terminal, escribir
```
pip install -r requirements.txt
```
Estas librerías son:
- Django versión 3.2.8
- djangorestframework-simplejwt versión 4.8.0
- psycopg2 versión 2.9.1
- PyJWT versión 2.1.0

2. Tener un servidor de PostgreSQL corriendo, con una base de datos para la cual haya se conozcan las credenciales de un usuario con permisos de creación de tablas en ésta.

3. Exportar las credenciales de la base de datos como _variables de entorno_: como se indica a continuación, entendiendo que cada nombre `<NOMBRE DE VARIABLE>` implica que se reemplace este texto por el valor que allí se indica
  - En Windows: si se está usando una terminal de PowerShell, ejecutar los siguientes comandos:
  ```
  $env:BACK_MECANO_USERS_TYPE = '<Tipo de servidor deseado: 'dev' para servidor de desarrollo, 'prod' para servidor de produccion>'
  $env:BD_US_NAME = '<Nombre de la base de datos>'
  $env:BD_US_USER = '<Usuario de la base de datos>'
  $env:BD_US_PASSWORD = '<Contraseña del usuario>'
  $env:BD_US_HOST = '<URL del servidor con la base de datos>'
  $env:BD_US_PORT = <Puerto para acceso a PostgreSQL>
  ```
  - En sistemas operativos basados en Unix:
  ```
  export BACK_MECANO_USERS_TYPE='<Tipo de servidor deseado: 'dev' para servidor de desarrollo, 'prod' para servidor de produccion>'
  export BD_US_NAME='<Nombre de la base de datos>'
  export BD_US_USER='<Usuario de la base de datos>'
  export BD_US_PASSWORD='<Contraseña del usuario>'
  export BD_US_HOST='<URL del servidor con la base de datos>'
  export BD_US_PORT=<Puerto para acceso a PostgreSQL>
  ```


4. Migrar las tablas necesarias a la base de datos: en el shell de comandos sobre la raiz ejecutar los siguientes comandos
```
python manage.py makemigrations
python manage.py migrate
```


## Instrucciones de uso

Una vez la aplicación ha sido instalada:

0. Abrir un shell de línea de comandos y ubicar su directorio en la raiz de este repositorio en el servidor en el que se instaló la aplicación.

1. Exportar como variables de entorno las credenciales de la base de datos, para un usuario con permisos de selección, inserción y eliminación de datos en sus tablas.

2. Ejecutar la aplicación y habilitar la comunicación con ésta a través de un puerto:
```
python manage.py runserver <Puerto para acceso a la aplicacion>
```
donde el puerto de acceso puede dejarse vacío, haciendo que por defecto se use el puerto `8000`.

3. Hacer uso de la RESTful web API que permite comunicación con la aplicación a través de la URL de servidor de la aplicación y el puerto indicado. Desde el mismo servidor, y utilizando el puerto por defecto, la URI de acceso a la API será: `http://127.0.0.1/localhost`.

## API

Los siguientes endpoints están habilitados para realizar peticiones HTTP a la aplicación:

- `login/`
  - Petición tipo `POST`: Permite la autenticación de un usuario registrado en la aplicación al adjuntar como cuerpo de la petición un texto tipo `JSON` con la siguiente estructura:
```
{
    "correo": "<Correo del usuario>",
    "password": "<Contraseña>"
}
```
  Si el usuario es autenticado correctamente, la respuesta a la petición contiene tokens de acceso y de actualización con la siguiente estructura:
```
{
    "access": "<Token de acceso>",
    "refresh": "<Token de actualización de tokens de acceso>"
}
```
- `user/`
  - Petición tipo `POST`: permite la creación de un nuevo usuario al adjuntar como cuerpo de la petición un texto tipo `JSON` con la siguiente estructura:
```
{
    "nombre": "<Nombre completo del usuario>",
    "usuario": "<Nombre de usuario>",
    "correo": "<Correo>",
    "telefono": <Número de contacto>,
    "pais": "<País>",
    "departamento": "<Departamento, en caso de que el país sea Colombia>",
    "ciudad": "<Ciudad>",
    "password": "<Contraseña>",
    "is_staff": <true o false, con true para indicar que el usuario creado sea administrador de la aplicación>
}
```
    Si el usuario es creado exitosamente, el usuario es automáticamente autenticado y la respuesta de la petición HTTP retorna tokens de acceso y actualización con un cuerpo en formato JSON como se indicó en el numeral de `login/`
- `user/<id_usuario>/`:
  - Petición tipo `GET`: Requiere de que se aporte un _Bearer Token_ de acceso de un usuario autenticado. Trae la información del usuario autenticado siempre y cuando `id_usuario` coincida con su número de identificación único. El cuerpo de la respuesta a esta petición HTTP tiene un formato JSON con la siguiente estrutura:
```
{
    "id": <Número de identificación único del usuario autenticado>
    "nombre": "<Nombre completo del usuario>",
    "usuario": "<Nombre de usuario>",
    "correo": "<Correo>",
    "telefono": <Número de contacto>,
    "pais": "<País>",
    "departamento": "<Departamento, en caso de que el país sea Colombia>",
    "ciudad": "<Ciudad>",
    "administrador": <true o false, con true para indicar que el usuario creado sea administrador de la aplicación>
}
```

- `refresh/`:
  - Petición tipo `POST`: permite la creación de un token de acceso para un usuario, al aportar un token de actualizado válido de este usuario. El cuerpo de la petición debe tener la siguiente estructura tipo JSON:
 ```
{
    "refresh": <Token de actualización válido de un usuario>
}
 ```
    El cuerpo de la respuesta a esta petición HTTP tiene la siguiente estructura:
```
{
    "access": <Token de acceso válido para el usuario>
}
```

- `verifyToken/`:
  - Petición tipo `POST`: permite averiguar el número de identificación único del usuario que se encuentra autenticado. El cuerpo de la petición debe contener el token de acceso con el siguiente formato tipo JSON:
```
{
    "token": <Token de acceso válido para el usuario>
}

```
