# coding=utf-8

#===============================================================================
#    【SESSION 操作控制】
#    一、django有四种session实现方式
#        1.数  据  库：database-backed sessions
#        2.缓        存：cached sessions
#        3.文件系统：file-based session
#        4.cookie：cookie-based session
#    @author: Alim
#    @E-mail: talkyunyun@126.com
#===============================================================================

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# 导入自定义包
from libs.func import alert

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
     	
      	return alert('设置成功')
    
    return render_to_response('set.html', {})



# session 获取
def get(request):
    
    name = request.session['name']
    
    return HttpResponse('获取到session的name值为：' + name);