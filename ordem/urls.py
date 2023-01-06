from django.contrib import admin
from django.urls import path, include
from ordem import views

urlpatterns = [
    path('<pk>/ordens/', views.show_ordems, name='show_ordens'),
    path('<pk>/ordens_and_ini', views.show_ordems_and_ini, name='show_ordens_and_ini'),
    path('<pk>/ordens_and_cur', views.show_ordems_and_cur, name='show_ordens_and_cur'),
    path('<pk>/ordens_final', views.show_ordems_final, name='show_ordens_final'),
    path('<pk>/ordem_detail/<pk_2>', views.show_ordens_detail, name='show_ordens_detail'),

    path('<pk>/create_orden/', views.create_ordem, name='add_orden'),

    path('<pk>/confirm_ordem/<pk_2>/', views.confirm_ordem, name='ordem_confirm'),
    path('<pk>/confirm_ordem_2/<pk_2>/', views.confirm_omi, name='ordem_confirm_2'),
    path('<pk>/confirm_ordem_3/<pk_2>/', views.confirm_OMF, name='ordem_confirm_3'),

    path('<pk>/ordens_motorista', views.show_ordens_motorista, name='ordens_motorista'),

    # API
    path('<pk>/API/APIGetAllOrdem/', views.APIGetAllOrdem.as_view(), name='API-Get-All-Ordem'),
    path('<pk>/API/APIGetOrdemInstituicao/', views.APIGetOrdem.as_view(), name='API-Get-Ordem'),
    path('<pk>/API/APICreateOrdem/', views.APICreateOrdem.as_view(), name='API-Create-Ordem'),

    path('<pk>/API/APIGConfirmOrdem/', views.APIGConfirmOrdem.as_view(), name='API-G-Confirm-Ordem'),
    path('<pk>/API/APIGInicioOrdem/', views.APIGInicioOrdem.as_view(), name='API-G-Inicio-Ordem'),
    path('<pk>/API/APIGFinalizeOrdem/', views.APIGFinalizeOrdem.as_view(), name='API-G-Finalize-Ordem'),

]
