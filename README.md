# Django_ToDoApp

- Django Web开发  零基础学习 搭建待办清单网站 

- 根据[B站视频](https://www.bilibili.com/video/av24293644/?p=1)整理 

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

## 2.创建app和网页.txt
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
