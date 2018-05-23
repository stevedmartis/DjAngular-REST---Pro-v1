from cuentas.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,    
    EmailField,
    CharField,
    ValidationError
)
from django.db.models import Q

from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _

from rest_framework.compat import authenticate

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class UsuarioCrearActualizarSerializer(ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),
    message=" Ya existe un usuario con este correo", )])
    #email2 = EmailField(label = 'Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password'
        ]

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email,
            first_name = first_name
        )

        user_obj.set_password(password)
        user_obj.save()

        return validated_data


class UsuarioListarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

class UsuarioDetalleSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',

        ]


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:

            try:
                user_get = User.objects.get(email=email)


                username = user_get.username
                print(username)


                user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

                # The authenticate call simply returns None for is_active=False
                # users. (Assuming the default ModelBackend authentication
                # backend.)
                if not user:

                    raise serializers.ValidationError({'': 'Contraseña Incorrecta.'})

            except User.DoesNotExist:

                raise serializers.ValidationError({'': "Correo Electrónico Incorrecto."})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs