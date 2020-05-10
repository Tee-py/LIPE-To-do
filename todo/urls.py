from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name="login"),
    path('register/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addTask/', views.addTask, name="addTask"),
    path('editTodo/<int:task_id>', views.EditTodo, name='editTodo'),
    path('deleteTask/<int:task_id>', views.deleteTask, name='deleteTask'),
]