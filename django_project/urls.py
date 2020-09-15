from django.contrib import admin
from django.urls import path
from todo.views import homeView, addItem, deleteItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name="home"),
    path('addItem/', addItem, name='add-item'),
    path('deleteItem/<int:itemId>/', deleteItem, name='delete-item')
]
