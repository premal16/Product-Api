from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializers
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/product-list/',
        'Detail View' : '/product-detail/<int:id>',
        'Create' : '/product-create/',
        'Update' : '/product-update/<int:id>',
        'Delete' : '/product-delete/<int:id>',
    }

    return Response(api_urls);

@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def viewProduct(request,pk):
    product = Product.objects.get(id = pk)
    serializer = ProductSerializers(product)
    return Response(serializer.data)



@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def productUpdate(request,pk):
    product = Product.objects.get(id = pk)
    serializer = ProductSerializers(instance=product, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
def productDelete(request,pk):
    product = Product.objects.get(id = pk)
    product.delete()
    return Response('Delete this items')
