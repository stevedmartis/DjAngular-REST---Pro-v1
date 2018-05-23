from cuentas.models import User
#####
#SERIALIZERS imports
#####
from .serializers import (
    UsuarioSerializer, 
    UsuarioCrearActualizarSerializer, 
    UsuarioListarSerializer, 
    UsuarioDetalleSerializer
)

######
#VIEWS imports
######
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
#
#PERMISOS
#
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly


# class UserAPIViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsuarioSerializer
    


class UsuarioListarAPIView(ListAPIView):
    """
    Serializador para LISTAR TODOS LOS USUARIOS
    """
    queryset = User.objects.all()
    serializer_class = UsuarioListarSerializer
    permission_classes = [AllowAny]


class UsuarioCrearAPIView(CreateAPIView):
    """
    Serializador para crear un usuario
    """
    serializer_class = UsuarioCrearActualizarSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UsuarioDetalleByIdAPIView(RetrieveAPIView):
    """
    Serializador para ver detalles de un USUARIO por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'email'
    permission_classes = [IsAuthenticated]

class UsuarioEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un USUARIO por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioCrearActualizarSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        

class UsuarioEliminarAPIView(DestroyAPIView):
    """
    Serializador par eliminar un usuario por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class UserByEmail(RetrieveAPIView):
    """
    Serializador para ver detalles de un USUARIO por Email
    """
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'email'
    permission_classes = [AllowAny]