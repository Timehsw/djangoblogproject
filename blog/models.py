from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        '''
        文章内部类,指定文章的排序方式
        '''
        ordering=['-created_time','title']