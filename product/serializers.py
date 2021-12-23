from cpu.serializers import CPUSerializer
from company.serializers import CompanySerializer
from sub_category.serializers import SubCategorySerializer
from category.serializers import CategorySerializer
from rest_framework import serializers
from .models import Product
from sub_category.models import SubCategory
from company.models import Company
from cpu.models import CPU
from category.models import Category


class ProductGetSerializer(serializers.ModelSerializer):

    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(), source='category.name'
    # )
    # sub_category = serializers.PrimaryKeyRelatedField(
    #     queryset=SubCategory.objects.all(), source='sub_category.name'
    # )
    # company = serializers.PrimaryKeyRelatedField(
    #     queryset=Company.objects.all(), source='company.name'
    # )
    # cpu = serializers.PrimaryKeyRelatedField(
    #     queryset=CPU.objects.all(), source='cpu.name'
    # )

    category = CategorySerializer(read_only=True)
    sub_category = SubCategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    cpu = CPUSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'sub_category',
                  'company', 'cpu', 'color', 'price']


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'sub_category',
                  'company', 'cpu', 'color', 'price']
