from django.contrib import admin
from django.urls import path, include

from veiculo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/veiculos/', views.show_veiculos, name='veiculos_show'),
    path('<pk>/add_veiculo/', views.add_veiculo, name='create_veiculo'),
]
