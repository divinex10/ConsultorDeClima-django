from django.shortcuts import render
from api_clima import info_clima, info_geo

def index(request):
    cidade = "Xique-Xique"

    estado = "BA"

    coordenadas = info_geo(cidade, estado)

    latitude, longitude = coordenadas

    clima = info_clima(latitude, longitude)

    return render(request, 'index.html', {'clima':clima})