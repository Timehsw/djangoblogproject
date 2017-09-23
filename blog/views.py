from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category,Tag


def index(request):
    '''
    博客首页处理函数
    :param request:
    :return:
    '''
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

