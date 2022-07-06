from django.shortcuts import render
from equipApi.models import TbEquipment
from .serializers import EquipmentSerializer, DetailSerializer, CreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

class equipView(ListAPIView):
    queryset = TbEquipment.objects.all()
    serializer_class = EquipmentSerializer

class detailView(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TbEquipment.objects.all()
    serializer_class = DetailSerializer

class updateView(UpdateAPIView):
    lookup_field = 'no'
    queryset = TbEquipment.objects.all()
    serializer_class = EquipmentSerializer

class deleteView(DestroyAPIView):
    lookup_field = 'no'    
    queryset = TbEquipment.objects.all()
    serializer_class = EquipmentSerializer

class createView(CreateAPIView):
    queryset = TbEquipment.objects.all()
    serializer_class = CreateSerializer