import pandas 
import datetime as dt
import random
import smtplib


data = pandas.read_csv("Day32 BirthdayWisher Program/Automated Birthday wisher/birthdays.csv")
birthdays = data.to_dict(orient="records")

letters = []
for n in range(3):
    with open(f"Day32 BirthdayWisher Program/Automated Birthday wisher/letter_templates/letter_{n+1}.txt" , 'r') as letter_files:
        letter = letter_files.read()
    letters.append(letter)


current = dt.datetime.now()
current_date = current.day
current_month = current.month
my_email = "hustleyt52@gmail.com"      
password = "hustlegaming"
for n in range(len(birthdays)):
    if birthdays[n]['day'] == current_date and birthdays[n]['month'] == current_month: 
        wish = random.choice(letters)
        wish = wish.replace('[NAME]',birthdays[n]['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email , password=password)
            connection.sendmail(from_addr=my_email , to_addrs=birthdays[n]['email'] , msg=f"Subject:Birthday Wishes..\n\n{wish}")

    



    










