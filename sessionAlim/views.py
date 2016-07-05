# coding=utf-8

#===============================================================================
#  SESSION 操作控制
#===============================================================================

from django.shortcuts import render_to_response

# session 操作首页
def index(request):
    
    return render_to_response('index.html', {})


# session 设置
def set(request):
    
    return


# session 获取
def get(request):
    
    return