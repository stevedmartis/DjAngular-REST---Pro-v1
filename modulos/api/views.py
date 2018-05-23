from rest_framework import viewsets
from modulos.models import Modulo
from .serializers import (
    ModuloSerializer, 
    ModuloListSerializer,
    ModuloCrearActualizarSerializer,
    ModuloDetalleSerializer,
    ModuloCrearActualizarSerializer
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)

#IMPORT PERMISOS
from rest_framework.permissions import AllowAny
class ModuloViewset(viewsets.ModelViewSet):
    """
    Viewset Generico que soporta todos los métodos HTTP [GET,POST,PUT,PATCH,DELETE,ETC].
    Vamos a dividirlo en API ENDPOINTS diferentes para cada operación.
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class ModuloListAPIView(ListAPIView):
    """
    View que permite solo leer la lista de modulos 
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloListSerializer
    permission_classes = [AllowAny]

class ModuloCreateAPIView(CreateAPIView):
    """
    View que permite un POST (crear) un modulo
    """
    queryset = Modulo.objects.all() #??
    serializer_class = ModuloCrearActualizarSerializer
    permission_classes = [AllowAny]

class ModuloDetalleAPIView(RetrieveAPIView):
    """
    View para ver el detalle de un modulo, a traves del ID(pk)
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ModuloEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un modulo por ID
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloCrearActualizarSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email
class ModuloEliminarAPIView(DestroyAPIView):
    """
    Serializador par eliminar un modulo por ID
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"