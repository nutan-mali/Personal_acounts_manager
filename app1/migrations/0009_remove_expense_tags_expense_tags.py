# Generated by Django 4.2 on 2024-04-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_expense_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='tags',
        ),
        migrations.AddField(
            model_name='expense',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='expenses', to='app1.tag'),
        ),
    ]