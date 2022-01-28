# from dataclasses import field
# from pyexpat import model
# from statistics import mode
from unicodedata import category
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
