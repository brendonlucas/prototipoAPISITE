from django.contrib import admin
from django.urls import path, include

from veiculo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/veiculos/', views.show_veiculos, name='veiculos_show'),
    path('<pk>/veiculos/<pk_2>/details', views.details_veiculo, name='details_veiculo'),
    path('<pk>/add_veiculo/', views.add_veiculo, name='create_veiculo'),
]
