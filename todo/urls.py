from django.urls import path
from . import views
from todo.views import todoView, addItem, deleteItem

urlpatterns = [
    path('', views.todoView, name="todo-home"),
    path('addItem/', views.addItem, name='add-item'),
    path('deleteItem/<int:itemId>/', views.deleteItem, name='delete-item')
]
