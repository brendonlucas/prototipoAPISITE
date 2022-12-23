from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as v
from instituicao import views


urlpatterns = [
    path('instituicao', views.show_instituicao, name='inst_show'),

    path('create_inst', views.create_instituicao, name='create_inst'),


]

