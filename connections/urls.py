from django.urls import path
from . import views
from connections.views import connectionView

urlpatterns = [
    path('', views.connectionView, name="connections-main")
]
