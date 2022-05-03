from rest_framework import serializers
from .models import User, FoodData, IntakeData, WaterConsumption

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FoodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodData
        fields = '__all__'

class IntakeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntakeData
        fields = '__all__'


class WaterCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterConsumption
        fields = '__all__'
