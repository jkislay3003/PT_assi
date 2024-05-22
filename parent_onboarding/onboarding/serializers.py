from rest_framework import serializers
from .models import User, Child, Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
