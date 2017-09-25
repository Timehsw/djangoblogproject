from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
# Create your models here.

class Category(models.Model):
    '''
    博客分类
    '''
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    博客标签
    '''
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''
    博客本身
    '''
    title=models.CharField(max_length=70) # 文章标题
    body=models.TextField() #文章正文
    created_time=models.DateTimeField() # 文章创建时间
    modified_time=models.DateTimeField() # 文章修改时间
    excerpt=models.CharField(max_length=200,blank=True) # 文章摘要
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User)
    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    def save(self, *args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post,self).save(*args,**kwargs)

    class Meta:
        '''
        文章内部类,指定文章的排序方式
        '''
        ordering=['-created_time','title']

class AboutMe(models.Model):
    '''
    关于我的介绍部分
    '''
    content=models.TextField()
    views=models.PositiveIntegerField(default=0)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "aboutme"

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    class Meta:
        '''
        文章内部类,指定文章的排序方式
        '''
        ordering=['-created_time']