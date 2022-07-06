from django.db import models

# Create your models here.

class TbEquipment(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)
    equip_number = models.CharField(db_column='EQUIP_NUMBER', max_length=15)  # Field name made lowercase.
    equip_type_number = models.CharField(db_column='EQUIP_TYPE_NUMBER', max_length=3)  # Field name made lowercase.
    creater_name = models.CharField(db_column='CREATER_NAME', max_length=4, blank=True, null=True)  # Field name made lowercase.



class TbInformation(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)
    equip_type_number = models.CharField(db_column='EQUIP_TYPE_NUMBER', max_length=3)  # Field name made lowercase.
    equip_name = models.CharField(db_column='EQUIP_NAME', max_length=30)  # Field name made lowercase.
    equip_manual = models.CharField(db_column='EQUIP_MANUAL', max_length=200)  # Field name made lowercase.
    equip_notion = models.CharField(db_column='EQUIP_NOTION', max_length=100)  # Field name made lowercase.

