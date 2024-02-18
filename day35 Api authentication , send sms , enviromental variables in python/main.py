import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
api_key = os.environ.get("My_api_key")
#b632cba5fcf956a30f368a815b2396dd
own_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
City_name = "Indore,India"
# AC810c3bff901fdf 9ab0a4f5d48a6bdb10
account_sid = os.environ.get("my_sid")
auth_token = os.environ.get("My_token")
#a83fd9857b5331007fb8156600f2f7df


weather ={
"lat" : 75.8333,
"lon" : 22.7179,
"appid" : api_key
,"exclude" : "current,minutely,daily"

}
response = requests.get(url=own_endpoint , params= weather)
print(response.status_code)
response.raise_for_status()


weather_data = response.json()
is_rain = False

weather_slice = weather_data['hourly'][:12]
for hour in weather_slice:
    condition_code = hour['weather'][0]["id"]
    if int(condition_code) < 700:
        is_rain = True

if is_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid , auth_token , http_client=proxy_client)
    message = client.messages \
        .create( body="It's going to rain today. Remember to bring an ☂️.", from_="+15047085982" ,to='+916263038693'
        )
    print(message.status)
