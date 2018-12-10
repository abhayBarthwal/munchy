from datetime import datetime, timedelta
from django.core.exceptions import *
from django.contrib.auth.hashers import *
import requests
from .models import *
from django.http import Http404
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import serializers


class YourSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   categories = serializers.ListField()
   bestseller = serializers.ListField()
   display = serializers.ListField()
   weekly = serializers.ListField()
   item = serializers.ListField()

def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

@api_view(['GET', 'POST', ])
@permission_classes((permissions.AllowAny,))
def index(request):
    categories = Category.objects.values_list('name','thumbnail')
    bestseller = Item.objects.values_list('name','price').filter(bestseller=1)
    display = Display.objects.values_list('scroll1','scroll2', 'scroll3', 'description')
    weekly = Item.objects.values_list('name','price').filter(weekly=1)
    item = Item.objects.values_list('name','price')
    context = [{'categories': categories, 'bestseller':bestseller, 'display':display, 'weekly':weekly, 'item':item}]
    results = YourSerializer(instance=context, many=True)
    return Response(json.dumps(results.data))

@api_view(['GET', 'POST', ])
@permission_classes((permissions.AllowAny,))
def order(request):
    mail = request.GET.get('mail', None)
    name = request.GET.get('name', None)
    mobile = request.GET.get('mobile', None)
    address = request.GET.get('address', None)
    itemlist = request.GET.get('itemlist', None)
    Orders.objects.create(address=address,name=name,mobile=mobile, mail=mail,itemlist=itemlist)

    return True

