from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
from comments.forms import CommentForm
import markdown

def index(request):
    '''
    博客首页处理函数
    :param request:
    :return:
    '''
    post_list=Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    '''
    博客详情页
    :param request:
    :param pk:
    :return:
    '''
    post=get_object_or_404(Post,pk=pk)

    # 阅读量 +1
    post.increase_views()
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    form=CommentForm()
    # 获取这篇post下的全部评论
    comment_list=post.comment_set.all()
    context={
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request,'blog/detail.html',context=context)


def archives(request,year,month):
    '''
    博客归档
    :param request:
    :param year:
    :param month:
    :return:
    '''
    post_list=Post.objects.filter(created_time__year=year,
                                  created_time__month=month
                                  ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    '''
    博客分类
    :param request:
    :param pk:
    :return:
    '''
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


def about(request):
    return render(request,'blog/about.html')
