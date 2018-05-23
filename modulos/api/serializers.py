from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer
)
from modulos.models import Modulo

from cuentas.api.serializers import UsuarioSerializer


class ModuloSerializer(HyperlinkedModelSerializer):
    """
    Serializador caso general
    """
    usuario = UsuarioSerializer(many=True, read_only=True)
    class Meta:
        model = Modulo
        fields = ('id','usuario','url','nombre','subtitulo','descripcion','img')



class ModuloListSerializer(ModelSerializer):
    """
    Serializador solo listado
    """
    usuario = UsuarioSerializer(many = True, read_only = True)
    class Meta:
        model = Modulo
        fields = ('id','usuario','nombre','subtitulo','descripcion','img')

class ModuloCrearActualizarSerializer(ModelSerializer):
    """
    Serializador crear y updatear.
    Este caso no recibe los parametros como ID o USUARIO, 
    ya que no nos necesarios para crear un modulo
    """
    class Meta:
        model = Modulo
        fields = ('nombre','subtitulo','descripcion','img')

class ModuloDetalleSerializer(ModelSerializer):
    """
    Serializador que lista los detalles de un modulo
    """
    usuario = UsuarioSerializer(many = True, read_only = True)
    class Meta:
        model = Modulo
        fields = ('id', 'usuario', 'nombre','subtitulo', 'descripcion', 'img')

