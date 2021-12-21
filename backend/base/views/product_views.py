from django.shortcuts import render
from base.products import products
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from base.models import Product
from base.serializer import ProductSerializer

from rest_framework import status


@api_view(['GET'])
def getProducts(request):    
    products = Product.objects.all()
    ps=ProductSerializer(products,many=True)
    return Response(ps.data)
    # pass
    #Object of type module is not JSON serializable


@api_view(['GET'])
def getProduct(request,pk):
    product=Product.objects.get(_id=pk)
    ps=ProductSerializer(product,many=False)
    return Response(ps.data)
    # product=None
    # for pr in products:
    #     if pr['_id'] == pk:
    #         product = pr
    # return Response(product)
    