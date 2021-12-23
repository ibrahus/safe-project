from django.db import models

# Create your models here.


class CPU(models.Model):
    name = models.CharField(max_length=255)
    cors = models.PositiveSmallIntegerField()
    speed = models.CharField(max_length=255)

    def __str__(self):
        return self.name
