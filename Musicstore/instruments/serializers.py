from rest_framework import serializers
from .models import Instrument, Order
from django.contrib.auth.models import User
from rest_framework import serializers

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
def validate_username(self, value):
    if User.objects.filter(username=value).exists():
        raise serializers.ValidationError("Username already exists")
    return value