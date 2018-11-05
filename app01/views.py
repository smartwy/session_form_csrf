from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
user_list = {
	'wangye':'123456',
	'zhaomin':'abcd',
	'root': '123',
}

# def auth(func):
#     def wrap(request, *args, **kwargs):
#         # 如果未登陆，跳转到指定页面
#         if request.path == '/test/':
#             return redirect('http://www.baidu.com')
#         return func(request, *args, **kwargs)
#     return wrap
#
# @auth
# def test(request):
# 	pass
#################### session ########################
# @csrf_exempt
def login(request):
	if request.method == 'GET':
		return render(request, 'login.html', {'mes':'请登录：'})
	if request.method == 'POST':
		print('按钮ajax-send',request.META.get('HTTP_X_CSRFTOKEN'),'登录form-send',request.META.get('CSRF_COOKIE'))  # 获取cdrftoken
		u = request.POST.get("user")
		p = request.POST.get('pwd')
		# print(type(u))
		if u not in user_list.keys():
			raise ValueError("1001")
		uu = request.POST.get("Auser")
		pp = request.POST.get('Apwd')
		if u in user_list and user_list[u] == p:
			# 生成随机字符串
			# 写到用户cookie
			# 保存session
			# 在随机字符串对应的字典中设置相关内容
			request.session['username'] = u      # 设置session
			request.session['is_login'] = True   # 设置session
			if request.POST.get('rmb') == '1':
				request.session.set_expiry(10)    # 设置失效时间10秒 默认2周
			return redirect('/index/')
			# return render(request, 'index.html', {'mes': u})
		return render(request, 'login.html', {'mes':'用户名或密码错误！'})

class Foo():
	def render(self):
		return HttpResponse('ok')

def index(request):
	# 获取当前用户的随机字符串，
	# 根据字符串获取相关信息
	if request.session.get('is_login', None):
		return render(request, 'index.html', {'mes': request.session.get('username')})
		# return Foo()
	else:
		return render(request, 'login.html', {'mes':'未登录。'})

def logout(request):
	request.session.clear()                  # 清除session
	# return redirect('/login/')
	return render(request, 'index.html')    # 注销后返回index，如是电商，可设置无法添加物品到购物车，只可以查看物品

#################### cache ########################

# from django.views.decorators.cache import cache_page
# 单视图缓存10秒
# @cache_page(10) # 生效10秒
def cache(request):
	import time
	ctime = time.strftime('%H:%M:%S')
	return render(request, 'cache.html', {'time': ctime})

#################### signal ########################

def signal(request):
	from app01 import models
	import time
	# models.user_info.objects.create(name=time.strftime('%H:%M:%S'))
	obj = models.user_tables(name=time.strftime('%H-%M-%S'))
	obj.save()
	# 自定义信号，触发信号
	from signal_list_import import customise
	customise.send(sender='customise_signal', arg1=123, arg2=time.strftime('%H-%M-%S'))
	return HttpResponse('ok')

#################### form ########################

from django import forms
from django.core.exceptions import ValidationError
import re
from app01 import models
from django.forms import widgets
from django.forms import fields
def mobile_validate(value):
	mobile_re = re.compile(r'^(13[0-9]|15[0-9]|17[678]|18[0-9]|14[57])[0-9]{8}$')
	if not mobile_re.match(value):
		raise ValidationError('手机号码格式错误')

class FM(forms.Form):
	# 字段本身只做验证，字段里有插件根据attrs设置的参数生成html
	user_type_choice = (
		(0, u'普通用户'),
		(1, u'高级用户'),
		(2, u'私有用户'),
	)
	name = fields.CharField(error_messages={'required':'用户名不能为空！', 'invalid':'用户名不合法！'},
	                       # widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'用户名'}),
	                       widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': u'用户名'}),
	                        label='用户名:')

	pwd = fields.CharField(max_length=18,
							min_length=6,
							error_messages={'required':'密码不能为空！', 'max_length':'密码长度不得大于18！', 'min_length':'密码长度不得小于6'},
							# widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'密码'})
							widget=widgets.PasswordInput(attrs={'class': "form-control", 'placeholder': u'密码'})) # 支持密文显示

	phone = fields.CharField(validators=[mobile_validate, ], # 自定义验证规则，将前端获取的是传到mobile_validate处理
	                        error_messages={'required': u'手机不能为空'},
	                        widget=widgets.TextInput(attrs={'class': "form-control",
	                                                      'placeholder': u'手机号码'}))

	email = fields.EmailField(error_messages={'required':'邮箱不能为空！', 'invalid':'邮箱不合法！'},
							widget = widgets.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}))

	user_type = fields.IntegerField(widget=widgets.Select(choices=user_type_choice,
	                                                           attrs={'class':"form-control", 'style': 'color: blue'}))

	u_list = fields.MultipleChoiceField(choices=user_type_choice) # 多选

	f = fields.FilePathField(path='F:\\iso')

	ch = fields.MultipleChoiceField(choices=user_type_choice,
	                                widget=widgets.CheckboxSelectMultiple)

def fm(request):
	if request.method == 'GET':
		# 初始化数据,字典类型，key与FM内的fields相同
		default_value = {'name': 'root', 'pwd': '123456', 'phone': '18612345678', 'email': 'root@163.com', 'user_type': 0, 'u_list': ['0'], 'f': 'F:\\iso\\CentOS-7-x86_64-Everything-1611.iso', 'ch': ['0']}
		obj = FM(default_value) # 支撑{{ obj.as_p }}生成html模板等方法
		return render(request, 'fm.html',{'obj':obj}) # 支撑{{ obj.as_p }}生成html模板等方法

	if request.method == 'POST':
		obj = FM(request.POST)
		status = obj.is_valid()  # 验证后状态，False/True
		data = obj.cleaned_data  # 验证后返回的数据
		err = obj.errors  # 验证后错误信息
		ret = obj.errors.as_json()  # 转为json格式
		if status:
			print(obj.cleaned_data) # 返回数据(字典类型)
			# models.user_tables.objects.create(**obj.cleaned_data) # 插入数据库表
			obj = FM()
			return render(request, 'fm.html', {'obj':obj})
		return render(request, 'fm.html', {'obj': obj})

