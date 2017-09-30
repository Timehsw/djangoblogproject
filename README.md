
通过动手写个人博客,学习Django,Python,以及前端相关知识.

-----

# 环境部署
```
python manage.py runserver 0.0.0.0:8000
```
## 虚拟环境

```
source blogproject_env/bin/activate

deactivate
```

# Django常用命令
## Django应用命令

+ 创建django程序: django-admin startproject blogproject
+ 新建django应用: python manage.py startapp blog
+ 运行django工程: python manage.py runserver
+ 创建迁移数据库迁移文件: python manage.py makemigrations
+ 迁移数据库: python manage.py migrate
+ 创建django超级用户: python manage.py createsuperuser

## Django模型类常用方法

**进入调试数据库命令行: python manage.py shell**

### 增加数据
```
c = Category(name='category test')
c.save()
t = Tag(name='tag test')
t.save()
```
### 存取数据

objects 是我们的模型管理器

```
from blog.models import *

Category.objects.get(name='hadoop')
Category.objects.filter(name='hadoop')
Category.objects.all()

```

### 修改数据

先用get取到数据,然后修改完后,调用save保存.

```
p=Post.objects.get(title='django笔记')
p.title='django learning'
p.save()
```

### 删除数据

先用get获取到数据后,调用对象的delete方法即可删除数据
```
p=Post.objects.get(title='django笔记')
p.delete()
```

## Django模板部分笔记

1. 用 {{ }} 包起来的变量叫做模板变量

