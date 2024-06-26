from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='expenses' , null=True)

    def __str__(self):
        return self.description