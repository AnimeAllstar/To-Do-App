from django.urls import path
from . import views
from users.views import register

urlpatterns = [
    path('', views.register, name="register"),
]
