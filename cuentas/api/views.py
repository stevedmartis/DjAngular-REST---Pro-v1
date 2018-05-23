from cuentas.models import User
#####
#SERIALIZERS imports
#####
from .serializers import (
    UsuarioSerializer, 
    UsuarioCrearActualizarSerializer, 
    UsuarioListarSerializer, 
    UsuarioDetalleSerializer,
    AuthTokenSerializer
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
    RetrieveUpdateAPIView,

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




from rest_framework import parsers, renderers
from rest_framework.compat import coreapi, coreschema
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        print(user)

        context = {
            'token': token.key,
           
        }
        
        return Response(context)


obtain_auth_token = ObtainAuthToken.as_view()
