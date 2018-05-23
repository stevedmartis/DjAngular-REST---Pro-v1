
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as login_auth,
    logout as logout_auth,

    )

    
User = get_user_model()

from partys.models import Party

#####
#SERIALIZERS imports
#####
from .serializers import (
    PartySerializer,  
    PartyListSerializer, 
    PartyDetailSerializer,
    PartyCreateUpdateSerializer
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
    
class PartyListAPIView(ListAPIView):
    """
    Serializador para LISTAR TODOS LOS USUARIOS
    """
    queryset = Party.objects.all()
    serializer_class = PartyListSerializer
    permission_classes = [AllowAny]

class PartyCreateAPIView(CreateAPIView):
    """
    Serializador para crear un usuario
    """
    serializer_class = PartyCreateUpdateSerializer
    queryset = Party.objects.all()
    permission_classes = [IsAuthenticated]


class PartyDetailByIdAPIView(RetrieveAPIView):
    """
    Serializador para ver detalles de un USUARIO por ID
    """
    queryset = Party.objects.all()
    serializer_class = PartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class PartyEditAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un USUARIO por ID
    """
    queryset = Party.objects.all()
    serializer_class = PartyCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        

class PartyDeleteAPIView(DestroyAPIView):
    """
    Serializador par eliminar un usuario por ID
    """
    queryset = Party.objects.all()
    serializer_class = PartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

