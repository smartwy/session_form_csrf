#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from django.middleware.csrf import CsrfViewMiddleware # csrf的源码

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render

class Row1(MiddlewareMixin):
	def process_request(self, request):
		print('Row1->process_request')

	def process_view(self, request, callback, callback_args, callback_kwargs):
		print('Row1->process_view')

	def process_exception(self, request, exception):
		print('Row1->process_exception')

	def process_response(self, request, response):
		print('1woR->process_response')
		return response

class Row2(MiddlewareMixin):
	def process_request(self, request):
		print('Row2->process_request')
		if request.POST.get('user') == 'root':
			return render(request, 'pic2.html')

	def process_view(self, request, callback, callback_args, callback_kwargs):
		print('Row2->process_view')

	def process_exception(self, request, exception):
		print('Row2->process_exception')

	def process_response(self, request, response):
		print('2woR->process_response')
		return response

	def process_template_response(self, request, response):
		print('2woR->process_template_response')
		return response


class Row3(MiddlewareMixin):
	def process_request(self, request):
		print('Row3->process_request')

	def process_view(self, request, callback, callback_args, callback_kwargs):
		# request:请求信息, callback：函数名, callback_args：函数可变参数(元组调用), callback_kwargs：函数关键字参数(字典调用)
		print('Row3->process_view', callback.__name__)

	def process_exception(self, request, exception):
		print('Row3->process_exception')
		if isinstance(exception, ValueError):
			return render(request, 'login.html', {'mes':'用户名格式不合法！'})

	def process_response(self, request, response):
		print('3woR->process_response')
		if request.POST.get('rmb') == '1':
			return HttpResponse('您的有效时间过短')
		return response

	def process_template_response(self, request, response):
		print('3woR->process_template_response')
		return response