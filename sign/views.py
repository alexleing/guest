# -*- coding: utf8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
import bootstrap_toolkit

# Create your views here.


def index(request):
    return render(request, "index.html")


# def login_action(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)  # 登录
#             # return HttpResponseRedirect('/event_manage/')
#             response = HttpResponseRedirect('/event_manage/')
#             # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
#             request.session['user'] = username  # 将session信息记录到浏览器
#             return response
#             # return HttpResponse('login success!')
#         else:
#             return render(request, 'index.html', {'error': 'username or password not exit,pls try again!'})
#
#         if username == admin and password == 123456:
#             response = HttpResponseRedirect('/event_manage/')
#             request.session['user'] = username
#             return HttpResponseRedirect['/event_manage/']
#         else:
#             return render(request, "event_manage.html")
#
#     else:
#         return render(request, 'index.html', {'error': 'username or password not exit,pls try again!'})

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        # if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
        #     # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            return response

            # auth.login(request, user)  # 登录
            # return HttpResponseRedirect('/event_manage/')
        else:
            return render(request, 'index.html', {'error': 'username or password error, pls try again!'})


@login_required
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')    # 读取浏览器session
    return render(request, "event_manage.html", {"user": username, "events": event_list})


@login_required
def search_name(request):
    username = request.session.get('user', '')
    # search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #  如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        #  如果page不在范围内，取最后一页
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


# 签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {'event': event})


# 退出登录
@login_required
def logout(request):
    auth.logout(request)    # 退出登录
    response = HttpResponseRedirect('/index/')
    return response