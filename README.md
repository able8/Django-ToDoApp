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

## 11.增删改查
- 增删改查 用字典存储, 只要服务器开着...
- 如果是get请求怎么办? 
- request.POST 中不存在'待办事项'这个键
- 如果是post请求, 但用户不写内容怎么办? request.POST 中的'待办事项'这个键对应值为 空的字符串 ''
- 用GET方法删除,划掉真的对吗? 用隐藏的form
```
全局列表

{% for  in  %}

    {{ forloop.counter }}

    {% if  %}
        
    {% else %}
        
    {% endif %}

{% endfor %}

"{% url 'todolist:删除' forloop.counter %}"
{# del/<forloop_counter> #}
redirect()
```
## 12.bootstrap弹窗
- https://v4.bootcss.com/docs/4.0/components/alerts/
```
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Holy guacamole!</strong> You should check in on some of those fields below.
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>
```
- js
```
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
```
- Modal https://v4.bootcss.com/docs/4.0/components/modal/

## 13.数据库
- 数据库，建标
```
CREATE TABLE 待办事项表
(
    序号 INT NOT NULL AUTO_INCREMENT,
    待办事项 VARCHAR(100) NOT NULL,
    已完成 tinyint(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (序号) 
)ENGINE=InnoDB CHARSET=utf8;
```
- 增加数据
```
INSERT INTO 待办事项表 (待办事项) VALUES ('看电影');
INSERT INTO 待办事项表 (待办事项) VALUES ('逛街');
INSERT INTO 待办事项表 (待办事项) VALUES ('陪客户吃饭');
```
- 建表 和 增删改查 django都能帮我们搞定
- 设置数据库连接
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
- create Model
    - 创建Model类，用来描述表的构成: 有哪些列(待办事项,完成状态,序号...)
    - 这是给网站开发者看的
- makemigrations -> 中文:制作迁移文件
    - 例如:0001_initial.py 也是用来描述表的构成
    - django会利用这个文件来建表改表
    - 每次新增model(表) 或者 修改model(表的构成) 都要 makemigrations
    - 这是给django自己看的,它用这个文件来建表或修改表
- python manage.py sqlmigrate todolist 0001  不会真的建表,只是查看
    - 查看django用 0001_initial.py 文件, 转化成了什么sql语句(不同的数据库服务器,语句不一样)帮我们建表, todolist是app的名字
```
BEGIN;
--
-- Create model Todo
--
CREATE TABLE "todolist_todo" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
     "thing" varchar(50) NOT NULL,
      "done" bool NOT NULL
);
COMMIT;
```
- migrate -> 中文:迁移,即运行这个文件 0001_initial.py   真正在数据库中建表,或修改表的结构
- python mange.py shell
```
from todolist.models import Todo
Todo.objects.all() -> QuerySet 查询集合 简单理解为表中的所有数据 
                   -> 所有行的集合__str__  显示更友好,命令行以及admin界面
Todo.objects.count() -> 行的数量

a_row = Todo(thing='逛街', done=False) -> 创建一行数据, 但并未保存
a_row.save() -> 真正保存到库中
a_row.id -> 保存之后才有id(序号)

a_row.thing -> 获取这一行的 thing(待办事项) 的值

Todo.objects.filter(done=False) -> 获取 [[所有]] done 为 False 的行, 即未完成的事项, 结果是个集合
another_row = Todo.objects.get(thing='看电影') -> 获取 thing 为 看电影 的行,仅一行
get不到会报错

another_row.thing = '去超市' -> 修改这一行的thing为 '去超市'
another_row.save() -> 改完别忘了保存

another_row.delete() -> 删除这一行
Todo.objects.all() -> 看看现在有什么

exit()    ctrl+z 回车

Register Models -> 注册model  注册后, 可以通过django自带的app -> admin后台界面来管理表数据

a = Todo.objects.get(id=2)
a.delete()
```

## 14. git新建数据库分支
```
git checkout -b db-version
git push origin db-version # 把本地分支push到远程
git checkout master # 切换到master分支
```
