from rest_framework import serializers 
from main.models import user, manager
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = user
        fields = ('username',
                  'password',)

class ManagerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = manager
        fields = ('userid', 'webusername',
                  'webpwd', 'website',)