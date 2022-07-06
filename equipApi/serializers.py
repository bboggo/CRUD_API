from .models import TbEquipment, TbInformation
from rest_framework import serializers

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbEquipment
        fields = ('no', 'equip_number', 'equip_type_number', 'creater_name')

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbEquipment
        fields = ('no', 'equip_number', 'equip_type_number', 'creater_name')
    
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbEquipment
        fields = ('equip_number', 'equip_type_number', 'creater_name')



class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInformation
        fields = ('no', 'equip_type_number', 'equip_name', 'equip_manual', 'equip_notion')

class InformationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInformation
        fields = ('no', 'equip_type_number', 'equip_name', 'equip_manual', 'equip_notion')

class InformationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInformation
        fields = ('no', 'equip_type_number', 'equip_name', 'equip_manual', 'equip_notion')