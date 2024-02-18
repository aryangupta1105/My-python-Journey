import requests 
import datetime as dt

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 165
AGE = 18


app_id = "7eec1209"
api_key = "defeba4177610c5d807cbe038d8e61d5—"

api_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"


options = {
  'method': 'POST',
}
headers_data ={
    'x-app-id': app_id,
    'x-app-key':api_key
  }

input_data = {
    "query": input("How much did you exercise today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.get(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=input_data , headers= headers_data)
results = response.json()
print(results)
# print(response.text)
# var request = require('request');
# var options = {
#   'method': 'POST',
#   'url': 'https://trackapi.nutritionix.com/v2/natural/exercise',
#   'headers': {
#     'Content-Type': 'application/json',
#     'x-app-id': ,
#     'x-app-key':
#   },
#   body: JSON.stringify({
#     "query": "swam for 1 hour"
#   })