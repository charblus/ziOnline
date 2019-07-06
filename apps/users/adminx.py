# -*- coding: utf-8 -*-
import xadmin

from .models import EmailVerifyRecord

# class EmailVerifyRecordAdmin(object):
#     pass

# 创建admin的管理类,这里不再是继承admin，而是继承object


class EmailVerifyRecordAdmin(object):
  # 配置后台需要显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段---过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
