"""session_form_csrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path
from django.conf.urls import url
from app01 import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('test/(\d+)/', views.test), # path的正则
    path('login/', views.login), # session csrf
    path('index/', views.index), # session csrf
    path('logout/', views.logout), # session csrf
    # path('cache/', cache_page(10)(views.cache)), # 单视图缓存10秒
    path('cache/', views.cache), # 缓存
    path('signal/', views.signal), # 信号
    path('form/', views.fm), # form

]
