# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.


SOFTWARE_TYPE=(('A','TypeA'),('B','TypeB'))
TECHNOLOGY_TYPE=(('A','TypeA'),('B','TypeB'))

class SoftwareType(models.Model):
    TYPE_GRADE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    type_name = models.CharField(default="", max_length=100, verbose_name=u"类别名")
    type_grade = models.IntegerField(choices=TYPE_GRADE, verbose_name="类目级别")
    parent_grade = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别",
                                     related_name="sub_soft")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"软件分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.type_small


class TechnologyType(models.Model):
    TYPE_GRADE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    type_name = models.CharField(default="", max_length=100, verbose_name=u"类别名")
    type_grade = models.IntegerField(choices=TYPE_GRADE, verbose_name="类目级别")
    parent_grade = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别",
                                     related_name="sub_tech")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = u"技术分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.type_small


class EquipmentType(models.Model):
    TYPE_GRADE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    type_name = models.CharField(default="",max_length=100, verbose_name=u"类别名")
    type_grade = models.IntegerField(choices=TYPE_GRADE, verbose_name="类目级别")
    parent_grade = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别",
                                        related_name="sub_equip")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"设备分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.type_name