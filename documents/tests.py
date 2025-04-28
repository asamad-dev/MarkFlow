from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from documents.models import Document, Tag

class DocumentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.tag = Tag.objects.create(name="example")

    def test_create_document(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            "title": "Test Doc",
            "content": "Hello **Markdown**",
            "tag_ids": [self.tag.id]
        }
        response = self.client.post('/api/documents/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], "Test Doc")

    def test_fetch_documents(self):
        Document.objects.create(title="Existing Doc", content="Sample", user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get('/api/documents/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_login(self):
        response = self.client.post(f'/api/users/{self.user.id}/login/', {
            "username": "testuser",
            "password": "testpass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
