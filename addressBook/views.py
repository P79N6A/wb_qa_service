#encoding:utf-8

import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

logger = logging.getLogger(__name__)


# mysql数据库操作
@csrf_protect
def add(request):
    response_data = {}
    if request.method == 'GET':
        return render_to_response("addressBook/welcome.html", response_data,
                                  context_instance=RequestContext(request))
        # alls = AddressBook.objects.all()
        # address = AddressBook()
        # groupone = Group.objects.get(id=1)
        # groupone.delete()
        # # address.name='lisi'
        # # address.tel='10086'
        # # address.address='Beijing'
        # # address.qq='324123123'
        # # address.group=groupone
        # # address.save()
        # # alls = AddressBook.objects.get(id=1)
        # if alls:
        #     alls.delete()
        # print '-'


# get请求进入注册页面;
# Post请求注册,之后重定向到登录页面
@csrf_protect
def regist(request):
    response_data = {}
    if request.method == 'GET':
        return render_to_response("addressBook/regist.html", response_data,
                                  context_instance=RequestContext(request))

    if request.method == 'POST':
        name = request.POST.get('Name').strip()
        password = request.POST.get('Password').strip()
        email = request.POST.get('youxiang').strip()

        user = User.objects.create_user(username=name, password=password, email=email)
        print user.is_staff  # True
        user.save()
        return HttpResponseRedirect('/addressBook/login')


# 登录,之后重定向
def my_login(request):
    response_data = {}
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect('/addressBook/welcome')
        if request.user.is_anonymous():
            return render_to_response("addressBook/login.html", response_data,
                                  context_instance=RequestContext(request))

    if request.method == 'POST':
        name = request.POST.get('Name').strip()
        password = request.POST.get('Password').strip()

        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/addressBook/welcome')

#登出,之后重定向
def my_logout(request):
    response_data = {}
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect('/addressBook/login')  # 跳转到index界面

@login_required
def welcome(request):
    response_data = {}
    if request.method == 'GET':
        response_data['user'] = request.user
        return render_to_response("addressBook/welcome.html", response_data,
                                  context_instance=RequestContext(request))