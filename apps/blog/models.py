from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)


class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)






