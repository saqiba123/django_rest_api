from .models import product  
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from .serializers import productSerializers
from rest_framework import status

def product_detail(request):
    data = product.objects.all()  
    return render(request, "app/index.html", {'products': data})  # Changed variable name to 'products'

@api_view(['GET'])
def getData(request):
    # info = models.student.objects.all()
    # return Response(info)
    info = models.product.objects.all()
    serializer = productSerializers(info, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def postData(request):
    serializer = productSerializers(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response(serializer.data)
    else:
        print("not working")

