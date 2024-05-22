from rest_framework import viewsets
from .models import User, Child, Blog
from .serializers import UserSerializer, ChildSerializer, BlogSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def home_feed(self, request, pk=None):
        user = self.get_object()
        child = user.children.first()  # Simplification: assume one child per user

        if not child:
            return Response({"error": "No child found for this user"}, status=400)

        age_group = self.get_age_group(child.age)
        blogs = Blog.objects.filter(age_group=age_group)

        # Filter by gender
        if child.gender:
            blogs = blogs.filter(models.Q(gender=child.gender) | models.Q(gender='unisex'))

        # Filter by parent's preferences
        preferences = user.preferences
        if preferences:
            if 'content_type' in preferences:
                blogs = blogs.filter(content_type__in=preferences['content_type'])

        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_preferences(self, request, pk=None):
        user = self.get_object()
        try:
            preferences = request.data.get('preferences', {})
            if not isinstance(preferences, dict):
                return Response({"error": "Invalid format for preferences"}, status=status.HTTP_400_BAD_REQUEST)

            user.preferences = preferences
            user.save()
            return Response({"status": "preferences updated"})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_age_group(self, age):
        if age <= 1:
            return '0-1'
        elif age <= 3:
            return '2-3'
        elif age <= 5:
            return '4-5'
        return '6+'

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Create your views here.
