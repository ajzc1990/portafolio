from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # ¡ESTA LÍNEA ES LA CLAVE!
    path('proyecto/<int:pk>/', views.detalle_proyecto, name='detalle'),
]