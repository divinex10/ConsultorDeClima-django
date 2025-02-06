import requests

API_KEY = 'b274188bc5e9773a7a447f7fc220f0c6'


def info_geo(cidade, estado):
    global cidade_nome
    cidade_nome = cidade


    url = F'http://api.openweathermap.org/geo/1.0/direct?q={cidade},{estado},&limit=1&appid=b274188bc5e9773a7a447f7fc220f0c6'
    response_geograph = requests.get(url)

    if response_geograph.status_code == 200:
        info_geo = response_geograph.json()

        if info_geo:
            latitude = info_geo[0]['lat']
            longitude = info_geo[0]['lon']
            
            return latitude, longitude
    
        else:
            return 'Erro: Nenhuma localização encontrada'
    else: 
        return f'Erro na requisição da API de localização: {response_geograph.status_code}'

def info_clima(latitude, longitude):
    url_2 = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&lang=pt-br&units=metric'

    response_clima = requests.get(url_2)

    if response_clima.status_code == 200:
        info_clima = response_clima.json()
        temperatura = info_clima['main']['temp']
        tempo = info_clima['weather'][0]['main']

        # Strings
        temperatura = f'{temperatura:.2f}'

        
        return {
            'temperatura' : temperatura,
            'tempo' : tempo,
            'cidade' : cidade_nome

        }
    else:
        return f'Erro na API de clima: {response_clima.status_code}'
