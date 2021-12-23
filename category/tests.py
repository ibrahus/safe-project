from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Category

# Create your tests here.


# class CategoryTestCase(APITestCase):
#     url = reverse('category-list')

#     def set_up(self):
#         self.admin = User.objects.create_user(
#             'admin', 'admin@test.com', 'password123')
#         self.admin.save()
#         self.admin.is_staff = True
#         self.admin.save()
#         self.token = Token.objects.create(user=self.admin)
#         print(self.token.key)
#         self.api_authentication()

#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#     def test_category_create(self):
#         response = self.client.post(
#             self.url, {'name': 'test category'})
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_login_admin(self):
#         client = APIClient()
#         response = client.post(
#             '/api-token-auth/', {'username': 'admin', 'password': 'password123'})
#         self.assertEqual(response.status_code, 200)

class CategoryAdminTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            'admin', 'admin@test.com', 'password123')
        self.admin.save()
        self.admin.is_staff = True
        self.admin.save()

        token = Token.objects.create(user=self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_login_admin(self):
        # client = APIClient()
        response = self.client.post(
            '/api-token-auth/', {'username': 'admin', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)

    def test_create_category(self):
        response = self.client.post('/category/', {'name': 'test_category'})
        self.assertEqual(response.status_code, 201)

    def test_retrieve_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, category.name)

    def test_retrieve_category_by_id(self):
        category = Category.objects.create(name="test_category_by_id")
        response = self.client.get(f'/category/{category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, category.name)

    def test_update_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.put(
            f'/category/{category.id}/', {'name': 'test_update_category'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_update_category')

    def test_delete_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.delete(f'/category/{category.id}/')
        self.assertEqual(response.status_code, 204)


class CategoryUserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'user', 'user@test.com', 'password123')
        self.user.save()

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_login_user(self):
        response = self.client.post(
            '/api-token-auth/', {'username': 'user', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user(self):
        self.client.credentials()
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, category.name)

    def test_retrieve_category_by_id(self):
        category = Category.objects.create(name="test_category_by_id")
        response = self.client.get(f'/category/{category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, category.name)

    def test_user_cant_create_category(self):
        response = self.client.post('/category/', {'name': 'test_category'})
        self.assertEqual(response.status_code, 403)

    def test_user_cant_update_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.put(
            f'/category/{category.id}/', {'name': 'test_update_category'})
        self.assertEqual(response.status_code, 403)

    def test_user_cant_delete_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.delete(f'/category/{category.id}/')
        self.assertEqual(response.status_code, 403)
