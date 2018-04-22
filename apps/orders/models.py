# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from things.models import Equipment, Technology, Software, EquipmentType, SoftwareType, TechnologyType
from users.models import User

# Create your models here.

PAYMENT_METHOD = (
    ("微信", "微信"), ("支付宝", "支付宝"), ("网银", "网银")
)


class EquipmentOrder(models.Model):
    order_id = models.CharField(primary_key=True, unique=True, max_length=100, default="3123", verbose_name=u"订单号")
    payer = models.ForeignKey(User, related_name="equipment_payer", verbose_name=u"支付者")
    payer_acount = models.CharField(max_length=100, verbose_name=u'支付账户')
    payee = models.ForeignKey(User, related_name="equipment_payee", verbose_name=u"收款人")
    payee_acount = models.CharField(max_length=100, verbose_name=u'收款账户')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name=u"支付时间")
    product = models.ForeignKey(Equipment, verbose_name=u"产品")
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50, default=PAYMENT_METHOD[0],
                                      verbose_name=u"支付方式")
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"租赁金额")
    damages = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"赔偿金额")
    poundage = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"平台扣除")
    receipt = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"实际到账")
    note = models.TextField(default="", max_length=200, verbose_name=u"留言")
    comment = models.TextField(default="", max_length=200, verbose_name=u"备注")

    class Meta:
        verbose_name = "设备订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id


class SoftwareOrder(models.Model):
    order_id = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name=u"订单号")
    payer = models.ForeignKey(User, related_name="software_payer", verbose_name=u"支付者")
    payer_acount = models.CharField(max_length=100, verbose_name=u'支付账户')
    payee = models.ForeignKey(User, related_name="software_payee", verbose_name=u"收款人")
    payee_acount = models.CharField(max_length=100, verbose_name=u'收款账户')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name=u"支付时间")
    product = models.ForeignKey(Software, verbose_name=u"产品")
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50, default=PAYMENT_METHOD[0],
                                      verbose_name=u"支付方式")
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"租赁金额")
    damages = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"赔偿金额")
    poundage = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"平台扣除")
    receipt = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"实际到账")
    note = models.TextField(default="", max_length=200, verbose_name=u"留言")
    comment = models.TextField(default="", max_length=200, verbose_name=u"备注")

    class Meta:
        verbose_name = "软件订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id


class TechnologyOrder(models.Model):
    order_id = models.CharField(primary_key=True, unique=True, max_length=100, verbose_name=u"订单号")
    payer = models.ForeignKey(User, related_name="technology_payer", verbose_name=u"支付者")
    payer_acount = models.CharField(max_length=100, verbose_name=u'支付账户')
    payee = models.ForeignKey(User, related_name="technology_payee", verbose_name=u"收款人")
    payee_acount = models.CharField(max_length=100, verbose_name=u'收款账户')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name=u"支付时间")
    product = models.ForeignKey(Technology, verbose_name=u"产品")
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50, default=PAYMENT_METHOD[0],
                                      verbose_name=u"支付方式")
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"租赁金额")
    damages = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"赔偿金额")
    poundage = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"平台扣除")
    receipt = models.DecimalField(default=0.0, decimal_places=2, max_digits=12, verbose_name=u"实际到账")
    note = models.TextField(default="", max_length=200, verbose_name=u"留言")
    comment = models.TextField(default="", max_length=200, verbose_name=u"备注")

    class Meta:
        verbose_name = "技术订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id
