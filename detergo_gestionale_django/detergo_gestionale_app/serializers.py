from rest_framework import serializers

from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class OrdineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordine
        fields = "__all__"
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        
class ArticoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articolo
        fields = "__all__"
        
class ColoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colore
        fields = "__all__"
        
class DifettoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difetto
        fields = "__all__"
        
class CapoPortatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapoPortato
        fields = "__all__"