#generar código que se conecte a la API de OpenWeatherMap.org y obtenga el clima actual de la ciudad que el usuario ingrese.
#Autor: Matronc

# importar librerías
import requests
import json

# función para obtener el clima
def clima(ciudad):
    api_key = "92d575819c61c039e044b1eea9664027"  # Reemplaza con tu clave de API de OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construir la URL completa
    complete_url = base_url + "q=" + ciudad + "&appid=" + api_key + "&units=metric"
    
    # Hacer la solicitud a la API
    response = requests.get(complete_url)
    
    # Convertir la respuesta a JSON
    x = response.json()
    
    # Verificar si la respuesta contiene el campo "main"
    if "main" in x:
        y = x["main"]
        temperatura = y["temp"]
        presion = y["pressure"]
        humedad = y["humidity"]
        
        # Obtener la descripción del clima
        z = x["weather"]
        descripcion_clima = z[0]["description"]
        
        # Imprimir los resultados
        print(f"Temperatura: {temperatura}°C")
        print(f"Presión: {presion} hPa")
        print(f"Humedad: {humedad}%")
        print(f"Descripción del clima: {descripcion_clima}")
    else:
        print(f"Error: No se encontró información del clima para la ciudad {ciudad}")

# Entrada de usuario
#dame ejemplo de ciudad

ciudad = input("Ingrese la ciudad: ")

# Llamar a la función
clima(ciudad)