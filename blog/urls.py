# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/23.
'''

from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index')
]