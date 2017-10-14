from django.contrib import admin
from comments.models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    '''
    后台管理界面中,comment类的展示字段
    '''
    list_display=['name','email','url','text','created_time']

admin.site.register(Comment,CommentAdmin)