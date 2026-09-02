from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
    path("", views.inicio, name="inicio"),

    #Pagina dispositivo
    path(
        "dispositivos/", 
        views.catalogo, 
        name="catalogo",
    ),

    #Pagina dispositivo id
    path(
        "dispositivos/<int:dispositivo_id>/",
        views.dispositivo_numero,
        name="por_dispositivo",
    ),

    path(
        "zonas/",
        views.catalogo_zonas,
        name="catalogo_zonas",
        ),

]