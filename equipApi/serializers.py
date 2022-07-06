from .models import TbEquipment
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
    
