from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as v
from instituicao import views

urlpatterns = [
    path('instituicao', views.show_instituicao, name='inst_show'),
    path('create_inst', views.create_instituicao, name='create_inst'),
    path('relatorios', views.config_relatorios, name='conf_relatorios'),


    # path('API/', views.create_instituicao, name='create_inst'),
    path('<pk>/API/APIGIntituicao/', views.APIGerentInstituicao.as_view(), name='API-G-Instituicao'),
    path('API/APICreateIntituicao/', views.APIGInstituicao.as_view(), name='API-Create-Instituicao'),
    # path('create_inst', views.create_instituicao, name='create_inst'),

]
