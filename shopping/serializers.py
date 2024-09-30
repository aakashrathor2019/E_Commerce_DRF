from .models import Product
from rest_framework import serializers

class ProductSerilaizer(serializers.ModelSerializer):
  class Meta:
    model=Product
    fields=['id','name','desc','price','image','category','stock']