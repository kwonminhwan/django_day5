from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    path('new_todo',views.new, name='new_todo'),
    path('delete/<int:todo_pk>', views.delete, name='delete_todo'),
    path('update/<int:todo_pk>', views.update, name='update_todo'),
    path('update_input/<int:todo_pk>', views.update_input, name='update_input'),
]
