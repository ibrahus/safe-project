from category.serializers import CategorySerializer
from rest_framework import serializers
from .models import SubCategory
from category.models import Category


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']
