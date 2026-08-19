import requests

WEBHOOK_URL = "il_tuo_link_webhook"
URL_METEO = "https://wttr.in/TuaCitta?format=j1"

risposta = requests.get(URL_METEO)
dati = risposta.json()

temperatura = dati["current_condition"][0]["temp_C"]
messaggio = f"Oggi ci sono {temperatura} gradi!"

print(messaggio)
requests.post(WEBHOOK_URL, json={"content": messaggio})
