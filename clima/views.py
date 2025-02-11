from django.shortcuts import render
from api_clima import info_clima, info_geo

def index(request):
    chuva = ('Rain', 'Drizzle')

    sol = ('Clear',)

    nuvem = ('Clouds',)

    neve = ('Snow',)

    trovao = ('Thunderstorm',)


    cidade = "Cavalcante"

    estado = "GO"

    coordenadas = info_geo(cidade, estado)

    latitude, longitude = coordenadas

    clima = info_clima(latitude, longitude)

    return render(request, 'index.html', {'clima':clima, 'chuva': chuva, 'sol': sol, 'nuvem': nuvem, 'trovao': trovao, 'neve': neve})