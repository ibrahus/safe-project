from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Company

# Create your tests here.


class CopmanyAdminTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            'admin', 'admin@test.com', 'password123')
        self.admin.save()
        self.admin.is_staff = True
        self.admin.save()

        token = Token.objects.create(user=self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_company(self):
        response = self.client.post('/company/', {'name': 'Apple'})
        self.assertEqual(response.status_code, 201)

    def test_retrieve_company(self):
        company = Company.objects.create(name='Apple')
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, company.name)

    def test_retrieve_company_by_id(self):
        company = Company.objects.create(name='Apple')
        response = self.client.get(f'/company/{company.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, company.name)

    def test_update_company(self):
        company = Company.objects.create(name='Apple')
        response = self.client.put(f'/company/{company.id}/', {
            'name': 'Samsung'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Samsung')

    def test_delete_company(self):
        company = Company.objects.create(name='Apple')
        response = self.client.delete(f'/company/{company.id}/')
        self.assertEqual(response.status_code, 204)


class CompanyUserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'user', 'user@test.com', 'password123')
        self.user.save()

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_unauthenticated_user(self):
        self.client.credentials()
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_company(self):
        company = Company.objects.create(name="Apple")
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, company.name)

    def test_retrieve_company_by_id(self):
        company = Company.objects.create(name="Apple")
        response = self.client.get(f'/company/{company.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, company.name)

    def test_user_cant_create_company(self):
        response = self.client.post('/company/', {'name': 'Apple'})
        self.assertEqual(response.status_code, 403)

    def test_user_cant_update_company(self):
        company = Company.objects.create(name="Apple")
        response = self.client.put(
            f'/company/{company.id}/', {'name': 'Samsung'})
        self.assertEqual(response.status_code, 403)

    def test_user_cant_delete_company(self):
        company = Company.objects.create(name="Apple")
        response = self.client.delete(f'/company/{company.id}/')
        self.assertEqual(response.status_code, 403)
