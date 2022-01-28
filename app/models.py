from operator import mod
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.





# --- Category SubCategory Model


class MainCategory(models.Model):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=5000)
    main_category = models.ForeignKey('MainCategory', on_delete=models.CASCADE)

# The main logic goes in admin.py
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=5000)
    main_category = models.ForeignKey('MainCategory', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


# The main logic goes in admin.py
    def __str__(self):
        return self.name
