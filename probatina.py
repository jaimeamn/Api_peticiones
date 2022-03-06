import requests

respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey")

print(respuesta.status_code)

data = respuesta.json()
print(data["rates"][3])
#print(respuesta.json())