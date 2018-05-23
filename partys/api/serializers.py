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

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as login_auth,
    logout as logout_auth,

    )

from partys.models import Party

User = get_user_model()


class PartySerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = ('id','username','email')


class PartyCreateUpdateSerializer(ModelSerializer):
    # email = EmailField(label = 'Email')
    #email2 = EmailField(label = 'Confirm Email')
    class Meta:
        model = Party
        fields = [
            'id',
            'name',

        ]

       
    #Aun sin validar
    def validate(self, data):
        return data

    def create(self, validated_data):
        name = validated_data['name']
        #first_name = validated_data['first_name']
        #email = validated_data['email']
        #password = validated_data['password']
        user_obj = Party(
            name = name,
        )
        return validated_data


class PartyListSerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = [
            'id',
            'name',
            'description',
			'status',
			'user',
			'place',
			'category'

        ]

class PartyDetailSerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = [
            'id',
            'name',

        ]

