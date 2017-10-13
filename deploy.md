# 部署过程

## 准备硬件
已经购买了VPS系统为ubuntu 14.04 64位,域名也已经购买好importthis.top

## 安装软件
我直接就用root用户了

1. 先更新一下系统

```
sudo apt-get update
sudo apt-get upgrade

```

2. 安装必要的软件 Nginx、Pytohn3、Git、pip 和 virtualenv
```
sudo apt-get install nginx
sudo apt-get install git python3 python3-pip
sudo pip3 install virtualenv
# 创建虚拟环境env
virtualenv --python=python3 env
# 激活进入虚拟环境
source env/bin/activate
# 退出虚拟环境
deactivate
```

3. 绑定域名和服务器IP
执行命令启动Nginx服务
```
service nginx start
service nginx stop
```

如果出现welcome to nginx! 那么说明Nginx启动成功了

4. 部署代码
```
# 激活虚拟环境,将全部依赖写入文件
pip freeze > requirements.txt
```
将代码上传到Github

进入项目内,安装全部依赖
```
pip install -r requirements.txt
```

5. 收集静态文件
```
python manage.py collectstatic
```
# 配置nginx
在sites-available目录下新建importthis.tip文件,也就是我的域名,名字随便取

```
root@husw:/etc/nginx/sites-available# pwd
/etc/nginx/sites-available
root@husw:/etc/nginx/sites-available# more importthis.top
server {
	charset utf-8;
	listen 80;
	server_name importthis.top;

	location /static {
		alias /root/sites/importthis.top/djangoblogproject/static;
	}

	location / {
		proxy_set_header Host $host;
		proxy_pass http://unix:/tmp/importthis.top.socket;
	}
}
```
我们在 /etc/nginx/sites-available/ 放置了配置文件，接下来需要创建一个符号链接，把这个配置文件加入到启用的网站列表中去，被启用网站的目录在 /etc/nginx/sites-enabled/，你可以理解为从 sites-available/ 目录下发送了一个配置文件的快捷方式到 sites-enabled/ 目录。具体命令如下：
```
ln -s /etc/nginx/sites-available/importthis.top /etc/nginx/sites-enabled/importthis.top
```

# 使用Gunicorn
1. 安装

```
pip install gunicorn
```

2. 用gunicorn启动blog
记住要记入到项目根目录下执行下面的命令

```
gunicorn --bind unix:/tmp/importthis.top.socket djangoblogproject.wsgi:application

```

浏览器输入域名，可以看到访问成功了！

3. 自动启动 Gunicorn
现在 Gunicorn 是我们手工启动的，万一哪天服务器崩溃重启了又得重新手工启动。为此我们写一个自动启动脚本，
这样当服务器重新启动后，脚本会帮我们重启 Gunicorn。先按 Ctrl + c 停止刚才启动的服务器进程。
写一个启动脚本，这样当服务器重启后能自动引导 Gunicorn 的启动。脚本位于 /etc/init/ 目录下，且脚本文件名必须以 .conf 结尾：
```
(env) root@husw:~/sites/importthis.top/djangoblogproject# more /etc/init/importthis.top.conf
start on net-device-up
stop on shutdown

respawn

setuid root
chdir /root/sites/importthis.top/djangoblogproject

exec ../env/bin/gunicorn --bind unix:/tmp/importthis.top.socket djangoblogproject.wsgi:application
```
+ start on net-device-up 确保只在服务器联网时才启动 Gunicorn。
+ 如果进程崩溃了（比如服务器重启或者进程因为某些以外情况被 kill），respawn 将自动重启 Gunicorn。
+ setuid 确保以 yangxg 用户的身份（换成你自己的用户名）运行 Gunicorn 进程。
+ chdir 进入到指定目录，这里进入项目的根目录。
+ exec 执行进程，即开启服务器进程。
现在可以用 start 命令启动 Gunicorn 了：
```
# 把刚才写的脚本的后缀.conf去掉,就可以用start命令启动了
(env) root@husw:~/sites/importthis.top/djangoblogproject# start importthis.top
importthis.top start/running, process 18807
```

# 注意
以后如果更新了代码，只要运行下面的命令重启一下 Nginx 和 Gunicorn 就可以使新的代码生效了：

```
sudo service nginx reload
sudo restart importthis.top
```

# 报错

blog运行起来后,但是静态资源类却没有加载进来.看nginx日志后发现没有访问权限
```
root@husw:/var/log/nginx# tail -f error.log
```
```
2017/10/13 05:22:58 [error] 16925#0: *23 open() "/root/sites/importthis.top/djangoblogproject/static/blog/js/script.js" failed (13: Permission denied), client: 114.248.231.240, server: importthis.top, request: "GET /static/blog/js/script.js HTTP/1.1", host: "importthis.top", referrer: "http://importthis.top/"

```

于是我把/root/sites/importthis.top/djangoblogproject/static整个递归赋了777的权限,但是还不行.

然后看nginx的进程用户,发现有些是www-data

```
root@husw:/etc/nginx# ps aux | grep nginx
root     16924  0.0  0.5  85852  1432 ?        Ss   05:10   0:00 nginx: master process /usr/sbin/nginx
www-data 16925  0.0  0.9  86484  2596 ?        S    05:10   0:00 nginx: worker process
www-data 16926  0.0  0.7  86132  1984 ?        S    05:10   0:00 nginx: worker process
www-data 16927  0.0  0.7  86132  1984 ?        S    05:10   0:00 nginx: worker process
www-data 16928  0.0  0.7  86132  1968 ?        S    05:10   0:00 nginx: worker process
root     17314  0.0  0.2   8828   780 pts/3    S+   05:28   0:00 grep --color=auto nginx
```

于是找到nginx的配置文件nginx.conf,发现第一行的user 后面就是www-data,于是我改成root
重启nginx后就成功了

```
root@husw:/etc/nginx# pwd
/etc/nginx
root@husw:/etc/nginx# more nginx.conf
user root;
worker_processes 4;
pid /run/nginx.pid;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
```