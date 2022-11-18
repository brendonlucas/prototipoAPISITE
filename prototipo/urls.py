from django.contrib import admin
from django.urls import path, include

handler404 = 'usuario.views.handler404'
handler500 = 'usuario.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('', include('veiculo.urls')),
    path('', include('ordem.urls')),
    path('', include('instituicao.urls')),
]

