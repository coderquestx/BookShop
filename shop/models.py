from django.utils import timezone
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()
    rewiews = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title