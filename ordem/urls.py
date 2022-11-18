from django.contrib import admin
from django.urls import path, include
from ordem import views





urlpatterns = [
    path('<pk>/ordens', views.show_ordems, name='show_ordens'),
    path('<pk>/create_orden', views.create_ordem, name='add_orden'),
    path('<pk>/confirm_ordem/<pk_2>/', views.confirm_ordem, name='ordem_confirm'),

]

# courses/<slug:param1>/<slug:param2>