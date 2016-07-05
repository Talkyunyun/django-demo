# coding=utf-8

#===============================================================================
#    【SESSION 操作控制】
#    一、django有四种session实现方式
#        1.数  据  库：database-backed sessions
#        2.缓        存：cached sessions
#        3.文件系统：file-based session
#        4.cookie：cookie-based session
#
#    ①、将session存储在数据中：
#        django的默认是存储在数据库中，实现方式实际上就是通过django中间件实现的。需要将“django.contrib.sessions”加入到INSTALLED_APPS变量中。然后运行python manage.py syncdb
#
#
#
#    @author: Alim
#    @E-mail: talkyunyun@126.com
#===============================================================================

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# session 操作首页
def index(request):
	
    return render_to_response('index.html', {})




#===============================================================================
#    如果不想使用官方提供的CSRF，可以使用一下的方式来关闭它
#    from django.views.decorators.csrf import csrf_exempt
#    @csrf_exempt
#===============================================================================
# session 设置
@csrf_exempt
def set(request):
    if request.method == 'POST':
    	name = request.POST['name']
     	request.session['name'] = name
    
    return render_to_response('set.html', {})



# session 获取
def get(request):
    
    name = request.session['name']
    
    return HttpResponse('获取到session的name值为：' + name);