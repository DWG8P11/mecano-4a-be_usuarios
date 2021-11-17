# Usando python 3
FROM python:3
# Crea el ambiente virtual
ENV PYTHONUNBUFFERED 1
# Crea una carpeta usuarios para guardar el backend dentro del ambiente virtual
RUN mkdir /usuarios_be
WORKDIR /usuarios_be
# Copia los archivos necesarios a la carpeta de usuarios_be
ADD . /usuarios_be/
# Instala los requerimientos en el nuevo ambiente virtual
RUN pip install -r requirements.txt
# Se dice que por el puente 8080 se podra entrar a esta maquina virtual
EXPOSE 8080
# Se escriben los comandos que se ejecutaran al prender la maquina virtual: migraciones y correr servidor
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT