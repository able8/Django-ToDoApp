from django.urls import path, include
from . import views

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/', views.edit, name='编辑'),
    path('del/<forloop_counter>', views.delete, name='删除'),
]