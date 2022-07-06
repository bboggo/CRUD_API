from django.shortcuts import render
from equipApi.models import TbEquipment, TbInformation
from .serializers import EquipmentSerializer, DetailSerializer, CreateSerializer, InformationCreateSerializer, InformationDetailSerializer, InformationSerializer
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



class inforView(ListAPIView):
    queryset = TbInformation.objects.all()
    serializer_class = InformationSerializer

class infordetailView(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TbInformation.objects.all()
    serializer_class = InformationDetailSerializer

class inforupdateView(UpdateAPIView):
    lookup_field = 'no'
    queryset = TbInformation.objects.all()
    serializer_class = InformationSerializer

class infordeleteView(DestroyAPIView):
    lookup_field = 'no'    
    queryset = TbInformation.objects.all()
    serializer_class = InformationSerializer

class inforcreateView(CreateAPIView):
    queryset = TbInformation.objects.all()
    serializer_class = InformationCreateSerializer