# coding=utf-8
#===============================================================================
# 存放自定义函数库
#===============================================================================
from django.http import HttpResponse

# 弹出提示函数
def alert(msg):
    
    return HttpResponse("<script>alert('"+ msg +"')</script>")