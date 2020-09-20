from django.urls import path
from . import views
from todo.views import todoView, addList, deleteList, starView

urlpatterns = [
    path('', views.todoView, name="todo-home"),
    path('addList/', views.addList, name='add-list'),
    path('deleteList/<int:itemId>/', views.deleteList, name='delete-list'),
    path('star/', starView, name='star-item'),
]
