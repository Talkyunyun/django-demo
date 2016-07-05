# coding=utf-8

from django.conf.urls import url

# 导入自定义APP
from sessionAlim import views as session



urlpatterns = [
    #===========================================================================
    # SESSION 相关操作
    #===========================================================================
    url(r'^session/$', session.index),
    url(r'^session/set/$', session.set),
    url(r'^session/get/$', session.get),
]