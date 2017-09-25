from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)

    # 表单提交数据一般都是通过POST请求
    if request.method == 'POST':
        # 用户提交的数据存在request.POST里面,这是个字段.利用表单构造CommentForm实例
        form=CommentForm(request.POST)
        # 校验表单数据的合法性
        if form.is_valid():
            # 将表单数据与文章关联行后才提交保存
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            # 重定向到post的详情页
            # 实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法
            return redirect(post)

        else:
            # 校验表单数据不合法,重新渲染详情页
            comment_list=post.comment_set.all()
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)

    return redirect(post)

