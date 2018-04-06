# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from things.models import Equipment, Software, Technology
from users.models import User

DEMAND_TYPE=(
    ("软件","软件"),("技术","技术"),("设备","设备"),
)


class EquipmentCollection(models.Model):
    collector = models.ForeignKey(User, verbose_name=u"收藏者")
    product=models.ForeignKey(Equipment,verbose_name="设备产品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "设备收藏"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.equip_name


class SoftwareCollection(models.Model):
    collector = models.ForeignKey(User, verbose_name=u"收藏者")
    product=models.ForeignKey(Software,verbose_name="软件产品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "软件收藏"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.software_name


class TechnologyCollection(models.Model):
    collector = models.ForeignKey(User, verbose_name=u"收藏者")
    product=models.ForeignKey(Technology,verbose_name="技术产品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "技术收藏"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.tech_name


class EquipmentIssue(models.Model):
    issuer = models.ForeignKey(User, verbose_name=u"发布者")
    product=models.ForeignKey(Equipment,verbose_name="设备产品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发布时间")

    class Meta:
        verbose_name = "设备发布"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.equip_name


class TechnologyIssue(models.Model):
    issuer = models.ForeignKey(User, verbose_name=u"发布者")
    product=models.ForeignKey(Technology,verbose_name="技术产品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发布时间")

    class Meta:
        verbose_name = "技术发布"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.tech_name


class SoftwareIssue(models.Model):
    issuer = models.ForeignKey(User, verbose_name=u"发布者")
    product=models.ForeignKey(Software,verbose_name="软件产品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发布时间")

    class Meta:
        verbose_name = "软件发布"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.software_name


class Demand(models.Model):
    demand_id = models.IntegerField(primary_key=True,verbose_name=u"需求ID")
    demander = models.ForeignKey(User,verbose_name=u"用户")
    type = models.CharField(default=DEMAND_TYPE[0],max_length=50,choices=DEMAND_TYPE,verbose_name=u"分类")
    title = models.CharField(default="",max_length=100,verbose_name=u"标题")
    content = models.TextField(default="",max_length=1000,verbose_name=u"内容")
    time = models.DateTimeField(default=datetime.now,verbose_name=u"时间段")
    money = models.CharField(default="", max_length=50,verbose_name=u"出租费用")

    class Meta:
        verbose_name = "需求发布"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title








