from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('',views.ModuloViewset) VIEWSET GENERICA PARA TODOS LOS CASOS


urlpatterns = [
    url(r'^$',views.ModuloListAPIView.as_view(),name='lista'),
    url(r'crear/$',views.ModuloCreateAPIView.as_view(),name='crear'),
    url(r'(?P<id>\d+)/$',views.ModuloDetalleAPIView.as_view(), name='detalle'),
    url(r'(?P<id>\d+)/editar/$',views.ModuloEditarAPIView.as_view(), name='editar'),
    url(r'(?P<email>\w+)/eliminar/$',views.ModuloEliminarAPIView.as_view(), name='eliminar'),
]