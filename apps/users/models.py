# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser

BANK = (("中国工商银行", "中国工商银行"), ("中国农业银行", "中国农业银行"),
        ("中国建设银行", "中国建设银行"), ("中国银行", "中国银行"),
        ("中国邮政储蓄银行", "中国邮政储蓄银行"),
        )

GENDER = (("男", u"男"), ("女", "女"), ("", ""))

EDUCATION = (("初中", "初中"), ("高中", "高中"),
             ("大学专科", "大学专科"), ("大学本科", "大学本科"),
             ("硕士", "硕士"), ("博士", "博士"), ("none", "")
             )


class User(AbstractUser):
    id = models.AutoField(primary_key=True, verbose_name=u"用户ID")
    nick_name = models.CharField(max_length=20, default="", null=False, blank=False, verbose_name=u"昵称")
    password = models.CharField(max_length=20, null=False, blank=False, verbose_name=u"密码")
    phone = models.CharField(max_length=11, null=False, blank=False, verbose_name=u"手机号", unique=True)
    complete = models.BooleanField(default=False, verbose_name=u"是否完善信息是否完善")
    # Complete
    user_name = models.CharField(max_length=10, default=u"", null=True, blank=True, verbose_name=u"用户姓名")
    identity = models.CharField(max_length=20, default=u"", null=True, blank=True, verbose_name=u"身份证号")
    bank = models.CharField(max_length=20, choices=BANK, default=BANK[0], null=True, blank=True, verbose_name=u"开户行")
    bank_number = models.CharField(max_length=30, default=u"", null=True, blank=True, verbose_name=u"银行卡号")
    gender = models.CharField(max_length=6, choices=GENDER, null=True, blank=True, default=GENDER[0])
    address = models.CharField(max_length=100, null=True, blank=True, default=u"")
    image = models.ImageField(upload_to="image/users/%Y/%m", default=u"users/default.png", null=True, blank=True,
                              max_length=100,
                              verbose_name="用户头像图片")
    # Selection
    education = models.CharField(max_length=20, choices=EDUCATION, default=u"none", null=True, blank=True,
                                 verbose_name="学历")
    qq = models.CharField(max_length=20, default="", null=True, blank=True, verbose_name="QQ号")
    wechat = models.CharField(max_length=30, default="", null=True, blank=True, verbose_name="微信号")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.nick_name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11,unique=True, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
