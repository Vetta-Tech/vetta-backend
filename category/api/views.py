from rest_framework import generics

from category.models import Category
from .serializers import CategoriesSerailizers


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerailizers
