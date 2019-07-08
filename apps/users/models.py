# -*- coding: utf-8 -*-
# 第一块区域import官方包
from datetime import datetime
# 第二块区域import第三方包
from django.db import models
from django.contrib.auth.models import AbstractUser
# 第三块区域import自己定义的


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField(
        '性别', max_length=10, choices=GENDER_CHOICES, default='female')
    adress = models.CharField('地址', max_length=100, default='')
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m',
                              default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register', '注册'),
        ('forget', '找回密码')
    )
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(
        choices=SEND_CHOICES, default='register', max_length=50, verbose_name='发送类型')
    # 这里的now得去掉(), 不去掉会根据编译时间。而不是根据实例化时间
    send_time = models.DateTimeField(
        default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name_plural = verbose_name = '邮箱验证码'

    def __str__(self):
        return '{}({})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y%m', max_length=100)
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
