# Generated by Django 4.2 on 2024-04-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='cost',
            field=models.IntegerField(),
        ),
    ]