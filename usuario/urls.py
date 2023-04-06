from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as v
from usuario import views
from usuario.views import CustomAuthToken

urlpatterns = [
    path('home', views.pag_home, name='pag'),
    path('<pk>/funcionarios', views.show_funcionarios_instituicao, name='show_funcionario'),
    path('login/', v.LoginView.as_view(template_name='home_page/home_page.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='home_page/home_page.html'), name="logout"),

    path('', views.show_home_page, name='show_home_page'),

    path('register', views.create_account, name="register"),
    path('<pk>/funcionarios/register_user/', views.create_account_func, name="register_new_user"),


    path('bancodados', views.criar_base_dados, name='create_bd'),
    path('<pk>/ccf', views.change_cargo_user, name='change_cargo_func'),
    path('profile', views.my_profile, name='profile_user'),
    path('<pk>/user/<pk_2>', views.get_profifle_user, name='profile_user_inst'),



    path('error/', views.error_data, name='error'),
    path('error404', views.error404, name='error404'),

    # API

    path('api-token-auth/', CustomAuthToken.as_view()),
    path('API/create_user/', views.APICreateUser.as_view(), name='create-acc-user'),
    path('<pk>/API/GetAllFuncInst/', views.APIGetAllFuncInst.as_view(), name='API-Get-All-Func-Inst'),
    path('<pk>/API/APIGetUserDetail/', views.APIGetUserDetail.as_view(), name='API-Get-User-Detail'),
    path('<pk>/API/APICreateFunc/', views.APICreateFunc.as_view(), name='API-Create-Func'),

]
