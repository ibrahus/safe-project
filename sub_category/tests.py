from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from category.models import Category
from .models import SubCategory

# Create your tests here.


class SubCategoryAdminTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            'admin', 'admin@test.com', 'password123')
        self.admin.save()
        self.admin.is_staff = True
        self.admin.save()

        token = Token.objects.create(user=self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_sub_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.post('/sub-category/', {
            'category': category.id,
            'name': 'test_sub_category',
        })
        self.assertEqual(response.status_code, 201)

    def test_retrieve_sub_category(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        response = self.client.get('/sub-category/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, sub_category.name)

    def test_retrieve_sub_category_by_id(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category_by_id",
            category=category
        )
        response = self.client.get(f'/sub-category/{sub_category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, sub_category.name)

    def test_update_sub_category(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        response = self.client.put(
            f'/sub-category/{sub_category.id}/', {
                'name': 'test_update_sub_category',
                'category': category.id
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_update_sub_category')

    def test_delete_sub_category(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        response = self.client.delete(f'/sub-category/{sub_category.id}/')
        self.assertEqual(response.status_code, 204)


class SubCategoryUserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'user', 'user@test.com', 'password123')
        self.user.save()

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_unauthenticated_user(self):
        self.client.credentials()
        response = self.client.get('/sub-category/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_sub_category(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        response = self.client.get('/sub-category/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, sub_category.name)

    def test_retrieve_sub_category_by_id(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category_by_id",
            category=category
        )
        response = self.client.get(f'/sub-category/{sub_category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, sub_category.name)

    def test_user_cant_create_sub_category(self):
        category = Category.objects.create(name="test_category")
        response = self.client.post(
            '/sub-category/', {
                'name': 'test_category',
                'category': category.id
            })
        self.assertEqual(response.status_code, 403)

    def test_user_cant_update_sub_category(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        response = self.client.put(
            f'/sub-category/{sub_category.id}/', {
                'name': 'test_update_sub_category',
                'category': category.id
            })
        self.assertEqual(response.status_code, 403)

    def test_user_cant_delete_category(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        response = self.client.delete(f'/sub-category/{sub_category.id}/')
        self.assertEqual(response.status_code, 403)
