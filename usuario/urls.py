from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as v
from usuario import views


urlpatterns = [
    path('home', views.pag_home, name='pag'),
    path('loginn', views.login_pag, name='login'),
    path('chiodosnegocio', views.home, name='home'),
    path('<pk>/funcionarios', views.show_funcionarios_instituicao, name='show_funcionario'),
    path('login/', v.LoginView.as_view(template_name='home_page/home_page.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='home_page/home_page.html'), name="logout"),

    path('', views.show_home_page, name='show_home_page'),

    path('register', views.create_account, name="register"),
    path('<pk>/funcionarios/register_user/', views.create_account_func, name="register_new_user"),


    path('bancodados', views.criar_base_dados, name='create_bd'),
    path('<pk>/ccf', views.change_cargo_user, name='change_cargo_func'),
    path('<pk>/profile', views.my_profile, name='profile_user'),

]
