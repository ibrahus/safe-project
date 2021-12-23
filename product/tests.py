from django.http import response
from product.models import Product
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from category.models import Category
from sub_category.models import SubCategory
from company.models import Company
from cpu.models import CPU

# Create your tests here.


class ProductAdminTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            'admin', 'admin@test.com', 'password123')
        self.admin.save()
        self.admin.is_staff = True
        self.admin.save()

        token = Token.objects.create(user=self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_product(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()

        response = self.client.post('/product/', {
            'name': 'new product',
            'category': category.id,
            'sub_category': sub_category.id,
            'company': company.id,
            'cpu': cpu.id,
            'color': "white",
            'price': '1000',
        })
        self.assertEqual(response.status_code, 201)

    def test_retrieve_product(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()
        product = Product.objects.create(
            name='new retrieve product',
            category=category,
            sub_category=sub_category,
            company=company,
            cpu=cpu,
            color="white",
            price='1000',
        )
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)

    def test_retrieve_product_by_id(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()
        product = Product.objects.create(
            name='new retrieve product by id',
            category=category,
            sub_category=sub_category,
            company=company,
            cpu=cpu,
            color="white",
            price='1000',
        )
        response = self.client.get(f'/product/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)

    def test_update_product(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()
        product = Product.objects.create(
            name='new retrieve product by id',
            category=category,
            sub_category=sub_category,
            company=company,
            cpu=cpu,
            color="white",
            price='1000',
        )
        response = self.client.put(f'/product/{product.id}/', {
            'name': 'updated_product',
            'category': category.id,
            'sub_category': sub_category.id,
            'company': company.id,
            'cpu': cpu.id,
            'color': "white",
            'price': '1000',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'updated_product')

    def test_delete_product(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()
        product = Product.objects.create(
            name='new delete product',
            category=category,
            sub_category=sub_category,
            company=company,
            cpu=cpu,
            color="white",
            price='1000',
        )
        response = self.client.delete(f'/product/{product.id}/')
        self.assertEqual(response.status_code, 204)


class ProductUserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'user', 'user@test.com', 'password123')
        self.user.save()

        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_unauthenticated_user(self):
        self.client.credentials()
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_product(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()
        product = Product.objects.create(
            name='new retrieve product',
            category=category,
            sub_category=sub_category,
            company=company,
            cpu=cpu,
            color="white",
            price='1000',
        )
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)

    def test_retrieve_product_by_id(self):
        category = Category.objects.create(name="test_category")
        sub_category = SubCategory.objects.create(
            name="test_sub_category",
            category=category
        )
        cpu = CPU.objects.create(name="cpu", cors=4, speed="3")
        company = Company.objects.create()
        product = Product.objects.create(
            name='new retrieve product by id',
            category=category,
            sub_category=sub_category,
            company=company,
            cpu=cpu,
            color="white",
            price='1000',
        )
        response = self.client.get(f'/product/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)

    def test_user_cant_create_product(self):
        response = self.client.post('/product/')
        self.assertEqual(response.status_code, 403)

    def test_user_cant_update_product(self):
        response = self.client.put('/product/')
        self.assertEqual(response.status_code, 403)

    def test_user_cant_delete_product(self):
        response = self.client.delete('/product/')
        self.assertEqual(response.status_code, 403)
