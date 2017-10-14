# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/10/13.
    desc: 自动化部署脚本
    在本地安装fabric :pip install fabric
    写好自动化脚本,在本地执行:fab deploy
    就会依次执行deploy函数里面的步骤,这样就可以在本地完成博客的部署,也不需要登录到服务器上了

    1.远程连接服务器。
    2.进入项目根目录，从远程仓库拉取最新的代码。
    3.如果项目引入了新的依赖，需要执行 pip install -r requirement.txt 安装最新依赖。
    4.如果修改或新增了项目静态文件，需要执行 python manage.py collectstatic 收集静态文件。
    5.如果数据库发生了变化，需要执行 python manage.py migrate 迁移数据库。
    6.重启 Nginx 和 Gunicorn 使改动生效。
'''

from fabric.api import env,run,task,runs_once,lcd,local,cd
from fabric.operations import sudo

GIT_REPO="https://github.com/Timehsw/djangoblogproject.git"

env.user='root'

# 填写你自己的主机对应的域名
env.hosts=['importthis.top']

# ssh 连接的22端口
env.port='22'

@runs_once
@task
def local_update():
    with lcd("/Users/hushiwei/PycharmProjects/djangoblogproject"):
        local("git add -A")
        local("git commit -m 'update'")
        local("git pull origin master")
        local("git push origin master")


@task
def remote_update():
    source_folder='/root/sites/importthis.top/djangoblogproject'

    with cd('cd %s' % source_folder):
        run("git checkout master")
        run("git pull origin master")
        run("""
            cd {} &&
            ../env/bin/pip install -r requirements.txt &&
            ../env/bin/python3 manage.py collectstatic --noinput &&
            ../env/bin/python3 manage.py migrate
            """.format(source_folder))
        run('restart importthis.top')
        run('service nginx reload')

@task
def deploy():
    local_update()
    remote_update()

