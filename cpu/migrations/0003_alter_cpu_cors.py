# Generated by Django 4.0 on 2021-12-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0002_alter_cpu_cors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='cors',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
