from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#-------------Se comenta ya que nos e esta utilizando, esta generaba una alerta--------#
#router.register('modulos',views.ModuloView)


# urlpatterns = [
#     path('',include(router.urls))
# ]
