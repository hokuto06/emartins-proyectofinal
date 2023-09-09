from django.urls import path
from MainSiteApp import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', views.inicio, name="Inicio"),
]