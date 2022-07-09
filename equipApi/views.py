from django.shortcuts import render
from equipApi.models import TbEquipment, TbInformation
from .serializers import EquipmentSerializer, DetailSerializer, CreateSerializer, InformationCreateSerializer, InformationDetailSerializer, InformationSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

# 기자재 정보 확인
class equipView(ListAPIView):
    queryset = TbEquipment.objects.all()
    serializer_class = EquipmentSerializer

# 기자재 디테일 정보 확인
class detailView(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TbEquipment.objects.all()
    serializer_class = DetailSerializer

# 기자재 수정
class updateView(UpdateAPIView):
    lookup_field = 'no'
    queryset = TbEquipment.objects.all()
    serializer_class = EquipmentSerializer

# 기자재 삭제
class deleteView(DestroyAPIView):
    lookup_field = 'no'    
    queryset = TbEquipment.objects.all()
    serializer_class = EquipmentSerializer

# 기자재 추가
class createView(CreateAPIView):
    queryset = TbEquipment.objects.all()
    serializer_class = CreateSerializer


# 기자재 종류 정보 확인
class inforView(ListAPIView):
    queryset = TbInformation.objects.all()
    serializer_class = InformationSerializer

# 기자재 종류 디테일 정보 확인
class infordetailView(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TbInformation.objects.all()
    serializer_class = InformationDetailSerializer

# 기자재 종류 정보 수정
class inforupdateView(UpdateAPIView):
    lookup_field = 'no'
    queryset = TbInformation.objects.all()
    serializer_class = InformationSerializer

# 기자재 종류 정보 삭제
class infordeleteView(DestroyAPIView):
    lookup_field = 'no'    
    queryset = TbInformation.objects.all()
    serializer_class = InformationSerializer

# 기자재 종류 정보 추가
class inforcreateView(CreateAPIView):
    queryset = TbInformation.objects.all()
    serializer_class = InformationCreateSerializer