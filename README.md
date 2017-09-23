 常用命令

## 虚拟环境

```
source blogproject_env/bin/activate

deactivate
```

## 创建django程序

```
django-admin startproject blogproject
```

## 新建django应用

```
python manage.py startapp blog
```

## 运行django工程

```
python manage.py runserver
```

## 创建迁移数据库迁移文件

```
python manage.py makemigrations
```

## 迁移数据库

```
python manage.py migrate
```

## 创建django超级用户

```
python manage.py createsuperuser
```

## 调试数据库

```
python manage.py shell
```

## 存取数据

objects 是我们的模型管理器

```
from blog.models import *

Category.objects.get(name='hadoop')
Category.objects.all()
```

## 修改数据

先用get取到数据,然后修改完后,调用save保存.

```
p=Post.objects.get(title='django笔记')
p.title='django learning'
p.save()
```

## 删除数据

先用get获取到数据后,调用对象的delete方法即可删除数据
```
p=Post.objects.get(title='django笔记')
p.delete()
```

## 模板

```
用 {{ }} 包起来的变量叫做模板变量
```