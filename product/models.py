from django.db import models
from category.models import Category
from sub_category.models import SubCategory
from company.models import Company
from cpu.models import CPU

# Create your models here.


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name='products')
    sub_category = models.ForeignKey(SubCategory,
                                     on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='products')
    cpu = models.ForeignKey(
        CPU, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
