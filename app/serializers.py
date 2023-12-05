from rest_framework import serializers
from app.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        # Hacemos correspondencia del serializador con la el modelo
        model = Usuario
        fields = ['Nombre','Apellido','Usuario','Clave','Correo']
