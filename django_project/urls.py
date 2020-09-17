from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/', include('users.urls')),
    path('', include('todo.urls')),
    path('todo/', include('todo.urls')),
]
