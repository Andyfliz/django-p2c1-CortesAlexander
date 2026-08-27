from django.shortcuts import render
from django.http import HttpResponse
from .services import cargar_dispositivos

def inicio(request):

    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )   

def dispositivo_numero(request, dispositivo_id):

    if dispositivo_id != 2:
        return HttpResponse(
            "Dispositivo no encontrado",
            status=404
        )

    dispositivos = [
        {"nombre": "ID del dispositivo", "estado": dispositivo_id},
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Inactivo"},
        {"nombre": "Climatizador", "estado": "Pendiente"},
    ]

    return render(
        request,
        "dispositivos/numero_dispositivo.html",
        {
            "dispositivo_id": dispositivo_id,
            "dispositivos": dispositivos,
        },
    )

def catalogo(request):
    dispositivos = cargar_dispositivos()
    activos = sum(
        1 for item in dispositivos
        if item["estado"] == "Activo"
    )
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
        }
    return render(
        request, "dispositivos/catalogo.html", contexto
    )


def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )
    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )


