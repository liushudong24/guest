from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# def index(request):
#     return HttpResponse("Hello Django!!!")
def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == '123':
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            # return HttpResponse('login error!!!')
            return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookies
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "event_manage.html", {"user": username})
