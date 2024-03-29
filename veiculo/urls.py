from django.contrib import admin
from django.urls import path, include

from ordem.views import APIGetOrdenVeiculo
from usuario.views import CustomAuthToken
from veiculo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/veiculos/', views.show_veiculos, name='veiculos_show'),
    path('<pk>/veiculos/<pk_2>/details', views.details_veiculo, name='details_veiculo'),
    path('<pk>/add_veiculo/', views.add_veiculo, name='create_veiculo'),

    # API
    path('<pk>/API/APIveiculos/', views.ApiVeiculoList.as_view(), name='veiculo-list'),
    path('<pk>/API/APIcreate_veiculo/', views.APICreateVeiculo.as_view(), name='create-veiculo'),
    path('<pk>/API/APIveiculo_detail/', views.ApiVeiculoDetail.as_view(), name='veiculo-Detail'),
    path('<pk>/API/APIget_ordem_veiculo/', APIGetOrdenVeiculo.as_view(), name='API-Get-Orden-Veiculo'),


]
