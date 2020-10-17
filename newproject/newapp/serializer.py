
from rest_framework import routers, serializers, viewsets
from newapp.models import User_Table
# from django.contrib.auth import User
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):

    phonenumber = serializers.CharField(source='user_information.Phone')
    Name = serializers.CharField(source='user_information.Name')
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User

        fields = ('password','password2','email', 'Name',
            'phonenumber',)