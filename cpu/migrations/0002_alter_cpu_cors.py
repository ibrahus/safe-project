# Generated by Django 4.0 on 2021-12-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='cors',
            field=models.IntegerField(),
        ),
    ]