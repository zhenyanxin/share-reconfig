# -*- coding: utf-8 -*-

import xadmin
from .models import User,VerifyCode
from xadmin import views


class BaseSetting(object):
    enable_themes = False
    use_bootswatch = False


class GlobalSettings(object):
    site_title = "地质设备共享后台管理系统"
    site_footer = "公司"
    menu_style = "accordion"


class UserAdmin(object):
    list_display = ['id', 'nick_name', 'phone']
    search_fields = ['id', 'nick_name', 'phone']
    list_filter = ['id', 'nick_name', 'phone']



class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']
    # search_fields = ['code', 'mobile']
    list_filter = ['code', 'mobile', 'add_time']


xadmin.site.register(User, UserAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)   # 注册主题
xadmin.site.register(views.CommAdminView, GlobalSettings)  # 注册全局
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
