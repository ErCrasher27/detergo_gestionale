from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class ClientiList(APIView):
    def get(self, request, format=None):
        cliente = Cliente.objects.all()[0:4]
        serializers = ClienteSerializer(cliente, many=True)
        return Response(serializers.data)
    
class OrdiniList(APIView):
    def get(self, request, format=None):
        ordine = Ordine.objects.all()[0:4]
        serializers = OrdineSerializer(ordine, many=True)
        return Response(serializers.data)
    
class CategorieList(APIView):
    def get(self, request, format=None):
        categoria = Categoria.objects.all()[0:4]
        serializers = CategoriaSerializer(categoria, many=True)
        return Response(serializers.data)
    
class ArticoliList(APIView):
    def get(self, request, format=None):
        articolo = Articolo.objects.all()[0:4]
        serializers = ArticoloSerializer(articolo, many=True)
        return Response(serializers.data)
    
class ColoriList(APIView):
    def get(self, request, format=None):
        colore = Colore.objects.all()[0:4]
        serializers = ColoreSerializer(colore, many=True)
        return Response(serializers.data)
    
class DifettiList(APIView):
    def get(self, request, format=None):
        difetto = Difetto.objects.all()[0:4]
        serializers = DifettoSerializer(difetto, many=True)
        return Response(serializers.data)
    
class CapiPortatiList(APIView):
    def get(self, request, format=None):
        capoPortato = CapoPortato.objects.all()[0:4]
        serializers = CapoPortatoSerializer(capoPortato, many=True)
        return Response(serializers.data)
