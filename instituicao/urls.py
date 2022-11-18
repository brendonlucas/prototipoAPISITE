from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as v
from instituicao import views


urlpatterns = [
    path('instituicao', views.show_instituicao, name='inst_show'),
    path('joinroom', views.entrar_intituicao, name='joinroom'),
    path('create_inst', views.create_instituicao, name='create_inst'),

    path('<pk>/reject-join', views.recuse_solicitacao, name='RejectJoin'),

]

