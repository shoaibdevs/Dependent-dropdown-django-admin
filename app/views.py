from rest_framework import generics
from .serializers import*
from .models import SubCategory
from .serializers import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Filter The Category By MainCategory Id
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['main_category']

    permission_classes = [IsAuthenticated]
