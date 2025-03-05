from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.URLField()

    def __str__(self):
        return self.title

