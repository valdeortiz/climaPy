import requests
from bs4 import BeautifulSoup

# direccion de meteorologia e hidrologia
def dmh():

    try:
        response = requests.get("https://www.meteorologia.gov.py/", timeout=10)
    except HTTPError as e:
        print(e)
        return 0,0

    try:
        soup = BeautifulSoup(response.content,"html.parser") #bs parsear el documento y response.content es para acceder a la respuesta del servidor,, y 2do para: el tipo de archivo que queremos parsear 
        forecast_today = soup.find(class_="forecast-today").get_text()
        forecast_today = forecast_today.replace("\n\n"," ").replace("\n","").strip().split()
        presion = " ".join(forecast_today[:3])
        sensacion_termica = " ".join(forecast_today[3:6])
        humedad = " ".join(forecast_today[6:9])
        viento = " ".join(forecast_today[9:12])
        result = f" {presion} \n {sensacion_termica} \n {humedad} \n {viento} "
        #verificar si es que retorna todos los datos
    except Exception as e:
        print(e)
        print("Error al leer el forecast_today")
        return 0,0	

    try:
        fecha = soup.find(class_="updated").get_text()
        fecha = fecha.replace("\n\n"," ").replace("\n","").strip()
        #verificar si es que retorna todos los datos
    except Exception as e:
        print(e)
        print("Error al leer la fecha")
        return result, 0

    return result , fecha

def crearJson():
    datosDmh, fechaDmh = dmh()
    #datosOp, fechaOp = openWeather()

    respjson = {
        "climapy": {
            "Direccion de meteorologia": {"datos": datosDmh, "fecha": fechaDmh}
            #"OpenWeather": {"datos": datosOp, "fecha": fechaOp}
        },
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    return json.dumps(
        respjson,
        indent=4,
        sort_keys=True,
        separators=(",", ": "),
    )

def leerJson():
    with open("climapy.json", "r") as f:
        response = f.read()
    return response


def run():
    response = crearJson()
    with open("climapy.json", "w") as f:
        f.write(response)

if __name__ == "__main__":
    result, fecha = dmh()
    #run()
    print(f"{fecha} \n{result} \n  ")
