from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class productCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup field = 'pk'