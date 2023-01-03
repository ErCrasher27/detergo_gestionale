from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class LatestClientiList(APIView):
    def get(self, request, format=None):
        cliente = Cliente.objects.all()[all]
        serializers = ClienteSerializer(cliente, many=True)
        return Response(serializers.data)
