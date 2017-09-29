from django.contrib import admin
from blog.models import Post,Tag,Category,Note

# Register your models here.
'''
django后台管理界面
哪些模型可以展示,展示哪些字段,由这里解决
'''
class PostAdmin(admin.ModelAdmin):
    '''
    后台管理界面中,post类的展示字段
    '''
    list_display = ['title','created_time','modified_time','category','author']

class NoteAdmin(admin.ModelAdmin):
    '''
    后台管理界面中,post类的展示字段
    '''
    list_display = ['name','views','created_time']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Note,NoteAdmin)
