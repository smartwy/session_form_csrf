#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception

from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate

from django.test.signals import setting_changed
from django.test.signals import template_rendered

from django.db.backends.signals import connection_created

# 自定义信号，定义信号
import django.dispatch
customise = django.dispatch.Signal(providing_args=["arg1", "arg2"])

def fun1(sender, **kwargs):
	print("exec_signal,pre_save")
	print(sender,kwargs)

def fun2(sender, **kwargs):
	print("exec_signal,pre_init")
	print(sender,kwargs)

def fun3(sender, **kwargs):
	print("exec_signal,post_init")
	print(sender,kwargs)

def fun4(sender, **kwargs):
	print("exec_signal,post_save")
	print(sender,kwargs['signal'])

# pre_init.connect(fun2)
# post_init.connect(fun3)
#
# pre_save.connect(fun1)
# post_save.connect(fun4)

# 自定义信号，注册信号
def signal_fun(sender, **kwargs):
	print('这是自定义信号触发的操作，')
	print(sender, kwargs)
customise.connect(signal_fun)


