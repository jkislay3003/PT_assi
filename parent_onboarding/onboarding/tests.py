import unittest
from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Child, Blog

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name="Test User", 
            email="test@example.com", 
            password_hash="hashed_password", 
            parent_type="first-time"
        )
        self.child = Child.objects.create(
            user=self.user,
            name="Test Child",
            age=2,
            gender="male"
        )
        self.blog = Blog.objects.create(
            title="Test Blog",
            content="This is a test blog",
            age_group="2-3",
            gender="male",
            content_type="blog"
        )

    def test_user_creation(self):
        response = self.client.post('/api/users/', {
            'name': 'New User',
            'email': 'new@example.com',
            'password_hash': 'new_hashed_password',
            'parent_type': 'experienced'
        })
        self.assertEqual(response.status_code, 201)

    # Additional tests for other CRUD operations and home feed

if __name__ == '__main__':
    unittest.main()


# Create your tests here.
