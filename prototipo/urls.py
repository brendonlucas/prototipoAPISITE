from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404

from prototipo import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('', include('veiculo.urls')),
    path('', include('ordem.urls')),
    path('', include('instituicao.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'usuario.views.handler404'
handler500 = 'usuario.views.handler500'

