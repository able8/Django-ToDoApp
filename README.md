# Django_ToDoApp

- Django Web开发  零基础学习 搭建待办清单网站 

- 根据[B站视频](https://www.bilibili.com/video/av24293644/?p=1)整理，简单易懂

## 1.前期准备

- 目标: 做一个 To Do List 待办事项清单网站
- 打开命令行, 安装虚拟环境
```
pip install virtualenv  # 安装virtualenv
```
- 建个 Django_venv 文件夹作为虚拟环境
```
cd Django_venv  # 进入该文件夹
virtualenv .  # 在当前文件夹构建虚拟环境
source bin/activate  # 激活虚拟环境
pip freeze  # 查看已安装的包
pip install django==2.0.5  # 安装django2.0.5
```

- 建个 Django_ToDoApp 文件夹存放所有django项目
```
cd Django_ToDoApp
django-admin startproject to_do_list  # 创建项目
cd to_do_list  # 进入项目文件夹
python manage.py runserver  # 启动服务器
# 在浏览器网址栏输入 localhost:8000
ctrl + c  # 关闭服务器
```

## 2.创建app和网页
- 激活虚拟环境
```
cd Django_venv # 到虚拟环境文件夹
source bin/activate  # 执行该文件
cd Django_ToDoApp/to_do_list  # 进入todo项目文件夹
python manage.py runserver  # 启动服务器
```
- 一个app负责一种功能
- 创建一个 todolist App 负责实现 待办事项 功能
```
python manage.py startapp todolist
```
- 注册该app,告诉服务器我存在
```
在settings.py INSTALLED_APPS 中加入
'todolist',
```
- 在这个app里面做个html网页,放在```templates```(网页模板)文件夹中


## 3.配置url和view
- 设置好网址, 给这个页面起个什么网址
- 当用户通过这个网址发出请求时，将网页发送给他
- 因为这个网页是待办事项网页, 网址设置和用户请求都让 todolist APP处理
```
to_do_list/to_do_list/urls.py [所有网址首先由它接手]
                       ||
                       ||
                      \  /
                       \/
to_do_list/todolist/urls.py [与待办事项相关的网址交给我接手]
                       ||
                       ||
                      \  /
                       \/
to_do_list/todolist/views.py [用户通过这些网址发出的请求的由我来处理]
```

## 4.bootstrap导航栏 
- https://v4.bootcss.com/docs/4.0/examples/  找到Navbar static 复制源代码
- 替换cdn
```
<link href="https://cdn.bootcss.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet">

<script src="https://cdn.bootcss.com/bootstrap/4.1.1/js/bootstrap.bundle.min.js"></script>
```

## 5.bootstrap表格
- https://v4.bootcss.com/docs/4.0/content/tables/

## 6.bootstrap表单

## 7.网址名,网页名

- 关于include()
- 大项目 -> 要避免网址名 网页名冲突
- render() 如何找到网页 ?
    - 根据所提供的网页名称,找所有的templates的文件夹,取第一个匹配的
- 网页名字重复怎么办?
```
    给个前缀
    建个新文件夹在templates下,以 app的名字 命名
    templates/app的名字/网页名字
    views.py -> return render(request, "todolist/home.html")

    <a href="hostname/urlpattern"></a>
```
- 想改网址怎么办?要改的地方好多o(╥﹏╥)o
```
    给网址起名字
    <a href="{% url 'url_name' %}"></a>  template tag{% tag_name  %}
```

- 网址名跟其他app里面的网址名字重复怎么办?
```
    给个前缀
    urls.py -> app_name = 'todolist'
    <a href="{% url 'todolist:url_name' %}"></a>
```
## 8.模版继承
- 我想改变导航栏的样式怎么办? 3个网页都要改?
    - Template inheritance
    - 做个模板html(所有网页的风格主题), 其他网页继承它,拓展它, 类似python的类继承
```
extends
{% extends "base.html" %}

block tag
{% block blockname %}

{% endblock blockname %}

three-level 大网站建议三级,小网站两级 

                              article.html
                            / 
             base_news.html  
           /                \
base.html                     live.html
           \
             base_sports.html
```

## 9.静态文件
- 新建static文件夹，存放 图片 css javascript
- 里面，再新建一个app文件夹，避免与其他app的static文件夹里面的静态文件冲突
```
app/static/app/images
app/static/app/js
app/static/app/css
app/static/app/icons


{% load static %}
{% static "路径" %}
```
## 10.处理用户请求
- request GET
- HTML form -> action="" method="POST"  button->submit
- {% csrf_token %}  跨站请求伪造
- name=""  给input的起名字
- request.POST是什么?  QueryDict
- content dictionary 在html中通过var访问字典
- {{ var }}  变量{{ }} 和标签{% %}  