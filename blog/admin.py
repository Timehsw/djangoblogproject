from django.contrib import admin
from blog.models import Post,Tag,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    '''
    后台管理界面中,post类的展示字段
    '''
    list_display = ['title','created_time','modified_time','category','author']
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
