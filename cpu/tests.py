from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import CPU
# Create your tests here.


class CPUAdminTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            'admin', 'admin@test.com', 'password123')
        self.admin.save()
        self.admin.is_staff = True
        self.admin.save()

        token = Token.objects.create(user=self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_cpu(self):
        response = self.client.post('/cpu/', {
            'name': 'M1',
            'cors': 8,
            'speed': "3 to 3.5 GH",
        })
        self.assertEqual(response.status_code, 201)

    def test_retrieve_cpu(self):
        cpu = CPU.objects.create(
            name="AMD",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.get('/cpu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, cpu.name)

    def test_retrieve_cpu_by_id(self):
        cpu = CPU.objects.create(
            name="Intel",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.get(f'/cpu/{cpu.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, cpu.name)

    def test_update_cpu(self):
        cpu = CPU.objects.create(
            name="Intel",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.put(f'/cpu/{cpu.id}/', {
            'name': 'M1 MAX',
            'cors': 8,
            'speed': "3 to 3.5 GH",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "M1 MAX")

    def test_delete_cpu(self):
        cpu = CPU.objects.create(
            name="Intel",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.delete(f'/cpu/{cpu.id}/')
        self.assertEqual(response.status_code, 204)


class CPUUserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'user', 'user@test.com', 'password123')
        self.user.save()

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_unauthenticated_user(self):
        self.client.credentials()
        response = self.client.get('/cpu/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_cpu(self):
        cpu = CPU.objects.create(
            name="AMD",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.get('/cpu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, cpu.name)

    def test_retrieve_cpu_by_id(self):
        cpu = CPU.objects.create(
            name="Intel",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.get(f'/cpu/{cpu.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, cpu.name)

    def test_user_cant_create_cpu(self):
        response = self.client.post('/cpu/', {
            'name': 'M1',
            'cors': 8,
            'speed': "3 to 3.5 GH",
        })
        self.assertEqual(response.status_code, 403)

    def test_user_cant_update_cpu(self):
        cpu = CPU.objects.create(
            name="AMD",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.put(
            f'/cpu/{cpu.id}/', {'name': 'M1'})
        self.assertEqual(response.status_code, 403)

    def test_user_cant_delete_category(self):
        cpu = CPU.objects.create(
            name="AMD",
            cors=10,
            speed="4 to 4.5 GH"
        )
        response = self.client.delete(f'/cpu/{cpu.id}/')
        self.assertEqual(response.status_code, 403)
