import datetime as dt
import smtplib
import random

with open("Day32 BirthdayWisher Program/quotes.txt" , 'r') as file:
    qoutes = file.readlines()

monday_qoute = random.choice(qoutes)
my_email = "hustleyt52@gmail.com"
password = "hustlegaming"
current = dt.datetime.now()
day_of_week = current.weekday()

if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email , password=password)
        connection.sendmail(from_addr=my_email , to_addrs=my_email , msg=f"Subject:The qoute of the day\n\n{monday_qoute}" )