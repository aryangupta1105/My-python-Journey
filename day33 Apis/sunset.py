import requests 
import datetime as dt
import time


My_Lat = 20.593683
My_Long = 78.962883
parameters_for_sunset = {
    'lat': My_Lat
    ,'lng' : My_Long
    ,'formatted' : 0
}

response = requests.get(url=" https://api.sunrise-sunset.org/json" , params=parameters_for_sunset)
# To format the time in 24 hour

response.raise_for_status()
data = response.json()
sunrise = int((data['results']['sunrise']).split("T")[1].split(":")[0])
sunset = int((data['results']['sunset']).split("T")[1].split(":")[0])


# api of iss location:
response2 = requests.get(url="http://api.open-notify.org/iss-now.json")
response2.raise_for_status()
data = response2.json()
lat = data['iss_position']['latitude']
lng = data['iss_position']['longitude']

current = dt.datetime.now()
current_time = str(current.time())
current_time = int(current_time.split(":")[0])

print(current_time)
def iss_near():
    if My_Lat-lat <= 5 or My_Lat-lat>=-5 and My_Long -lng<= 5 or My_Long-lng >= -5:
        return True
def is_dark():
    if sunset <= current_time or sunrise >= current_time:
        return True
my_mail = "hustleyt52@gmail.com"
password = "hustlegaming"
import smtplib
while True:
    time.sleep(60)
    if iss_near() and is_dark():
        with (smtplib.SMTP("smtp.gamail.com")) as connection:
            connection.starttls()
            connection.login(user=my_mail , password= password)
            connection.sendmail(from_addr=my_mail , to_addrs=my_mail , msg="Subject:Time to watch the iss\n\nThe iss is just above you go ahead and see it")
            


