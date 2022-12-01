from django.contrib import admin
from django.urls import path, include
from ordem import views





urlpatterns = [
    path('<pk>/ordens', views.show_ordems, name='show_ordens'),
    path('<pk>/ordens_and_ini', views.show_ordems_and_ini, name='show_ordens_and_ini'),
    path('<pk>/ordens_and_cur', views.show_ordems_and_cur, name='show_ordens_and_cur'),
    path('<pk>/ordens_final', views.show_ordems_final, name='show_ordens_final'),

    path('<pk>/create_orden', views.create_ordem, name='add_orden'),
    path('<pk>/confirm_ordem/<pk_2>/', views.confirm_ordem, name='ordem_confirm'),

]

# courses/<slug:param1>/<slug:param2>