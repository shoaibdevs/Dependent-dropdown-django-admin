from django.urls import  path
from .views import *

urlpatterns = [
    path('category/', CategoriesAPIView.as_view()),
]