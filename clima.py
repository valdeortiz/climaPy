import requests 
#import json
#import tkinter as tk

# win = tk.Tk()
# win.title("Clima")
# win.geometry("500x500")

# En el archivo apiId debemos colocar nuestro apiId de open weather
with open("apiId.txt","r") as apiId:
	api = apiId.read()
url = "http://api.openweathermap.org/data/2.5/weather?"

def weather():
 	#location = entry.get()
 	location = "Asunción,PY"
 	answer = url + "appid=" + api +"&q=" + location 
 	response = requests.get(answer)
 	res = response.json()
 	#print(res)
 	if res["cod"] != "404" :
 		x = res["main"]
 		temperature = x["temp"]
 		pressure = x["pressure"]
 		humidity = x["humidity"]
 		y = res["weather"]
 		whater_description = y[0]["description"]
 		print(f"Temperatura: {temperature} f \n presion atmoferica: {pressure}\n humedad: {humidity} \n descripcion: {whater_description}")
 		# label1 = tk.Label(win, text= f"temperature (in kelvin unit) = {tem}, \n"
 		# 							f"atomspheric pressure (in aPh unit) = {pre}, \n"
 		# 							f"humidity = {hum}, \n"
 		# 							f"description = {whater_description}")
 		# label1.grid(row=2,column=0)
 	else:
 		print("Error 404")
 		# label2 = tk.Label(win, text= f"Enter correct city")
 		# label2.grid(row=2,column=0)


weather()

# label = tk.Label(win, text="Enter city Name Here: ", bg="#add8e6")
# label.grid(row=0,column=0)
# label.config(font=("times",20,"bold"))

# entry = tk.Entry(win)
# entry.grid(row=1,column=0,padx=100)

# button = tk.Button(win, text="search", command=weather)
# button.grid(row=1,column=1)

#win.mainloop()


# {
# "id": 3474570,
# "name": "Asunción",
# "country": "PY",
# "coord": {
# "lon": -57.666672,
# "lat": -25.26667
# }
# },