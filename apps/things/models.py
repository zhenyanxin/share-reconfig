# _*_coding:utf-8_*_


from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from thing_types.models import EquipmentType,SoftwareType,TechnologyType
from users.models import User



class Equipment(models.Model):
    equip_id = models.AutoField(primary_key=True, verbose_name=u"设备ID")
    equip_type = models.ForeignKey(EquipmentType, verbose_name=u"设备类别")
    equip_name = models.CharField(max_length=100, verbose_name=u"设备名称")
    produce_date = models.DateTimeField(default=datetime.now, verbose_name=u"生产日期")
    equip_over = models.DateTimeField(default=datetime.now, verbose_name=u"到期年限")
    equip_owner = models.ForeignKey(User, verbose_name=u"设备所属")
    equip_expense = models.FloatField(default=0.0, verbose_name=u"设备价格")
    equip_start = models.DateTimeField(default=datetime.now, verbose_name=u"出租开始时间")
    equip_end = models.DateTimeField(default=datetime.now, verbose_name=u"出租结束时间")
    equip_price = models.DecimalField(max_digits=10,decimal_places=2, default=0.0, verbose_name=u"出租费用(元/天)")
    equip_picture = models.ImageField(upload_to="image/image_equipment/%Y/%m", default=u"image/image_equipment/default.png", max_length=100, verbose_name=u"设备图片")
    equip_parameter = models.TextField(verbose_name=u"性能参数")
    equip_place = models.CharField(max_length=50, verbose_name=u"地点")
    equip_comment = models.CharField(null=True, blank=True, max_length=300, verbose_name=u"备注")

    class Meta:
        verbose_name = u"设备"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.equip_name



class Software(models.Model):
    software_id = models.AutoField(primary_key=True, verbose_name=u"设备ID")
    software_type = models.ForeignKey(SoftwareType, verbose_name='软件类别')
    software_name = models.CharField(max_length=100, verbose_name=u"软件名称")
    software_owner = models.ForeignKey(User, verbose_name=u"软件所属")
    software_expense = models.FloatField(default=0.0, verbose_name=u"软件价格")
    software_start = models.DateTimeField(default=datetime.now, verbose_name=u"出租开始时间")
    software_end = models.DateTimeField(default=datetime.now, verbose_name=u"出租结束时间")
    software_price = models.DecimalField(max_digits=10,decimal_places=2, default=0.0, verbose_name=u"出租费用(元/天)")
    software_image = models.ImageField(upload_to="image/image_software/%Y/%m", default=u"image/image_software/default.png", max_length=100, verbose_name=u"软件图片")
    software_describe = models.TextField(verbose_name=u"软件描述")
    os = models.CharField(max_length=100, verbose_name=u"运行平台")
    software_comment = models.CharField(null=True, blank=True, max_length=300, verbose_name=u"备注")

    class Meta:
        verbose_name = u"软件"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.software_name


class Technology(models.Model):
    tech_id = models.AutoField(primary_key=True, verbose_name=u"技术ID")
    tech_type = models.ForeignKey(TechnologyType, verbose_name='技术类别')
    tech_name = models.CharField(max_length=100, verbose_name=u"技术名称")
    tech_info = models.CharField(max_length=300, verbose_name=u"技术服务信息")
    tech_owner = models.ForeignKey(User, verbose_name=u"技术所属")
    tech_price = models.DecimalField(max_digits=10,decimal_places=2, default=0.0, verbose_name=u"技术价格(元/天)")
    tech_image = models.ImageField(upload_to="image/image_technology/%Y/%m", default=u"image/image_technology/default.png", max_length=100, verbose_name=u"技术图片")
    tech_commet = models.CharField(null=True, blank=True, max_length=300, verbose_name=u"备注")

    class Meta:
        verbose_name = u"技术"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tech_name












