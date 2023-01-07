from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class CustomerList(APIView):
    def get(self, request, format=None):
        customer = Customer.objects.all()[0:4]
        serializers = CustomerSerializer(customer, many=True)
        return Response(serializers.data)
    
class OrderList(APIView):
    def get(self, request, format=None):
        order = Order.objects.all()[0:4]
        serializers = OrderSerializer(order, many=True)
        return Response(serializers.data)
    
class CategoryList(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()[0:4]
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)
    
class ItemList(APIView):
    def get(self, request, format=None):
        item = Item.objects.all()[0:4]
        serializers = ItemSerializer(item, many=True)
        return Response(serializers.data)
    
class ColorList(APIView):
    def get(self, request, format=None):
        color = Color.objects.all()[0:4]
        serializers = ColorSerializer(color, many=True)
        return Response(serializers.data)
    
class DefectList(APIView):
    def get(self, request, format=None):
        defect = Defect.objects.all()[0:4]
        serializers = DefectSerializer(defect, many=True)
        return Response(serializers.data)
    
class BroughtItemList(APIView):
    def get(self, request, format=None):
        broughtItem = BroughtItem.objects.all()[0:4]
        serializers = BroughtItemSerializer(broughtItem, many=True)
        return Response(serializers.data)
    
class ItemListByCategory(APIView):
    
    def get_object(self, idCategory):
        query = Item.objects.filter(id_category = idCategory)
        return query
        
    def get(self, request, idCategory):
        interface = self.get_object(idCategory)
        serializers = ItemSerializer(interface, many=True)
        return Response(serializers.data)