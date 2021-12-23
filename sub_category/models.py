from django.db import models
from category.models import Category

# Create your models here.


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
