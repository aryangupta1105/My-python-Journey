import requests
import datetime as dt
import math
import random
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "AC810c3bff901fdf9ab0a4f5d48a6bdb10"
auth_token = "a83fd9857b5331007fb8156600f2f7df"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#alphavintage
My_api_key = "GQ8A2V27ZPG1EGJL"
#newsapi
api_key = "1a1de6af0f7a47d18e09cbbdc740bb0b"



# Getting the dates:
current = dt.datetime.now()
current_date = current.date()

# According to the records
todays = current_date - dt.timedelta(days=1)
yesterday = current_date - dt.timedelta(days=2)

todays = str(todays)
yesterday = str(yesterday)

# For my way...
# days = [todays , yesterday ,day3, day4]
# Making the list of dates to get the correct date for news...







## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey={My_api_key}")
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# My way to do it:
# daily_closing = data["Time Series (Daily)"]
# for n in range(len(days)):
#     if days[n] in daily_closing:
#         todays = days[n]
#         yesterday = days[n-1]
# today_closing = daily_closing[todays]['4. close']
# yesterday_closing = daily_closing[yesterday]['4. close']
# print(today_closing)
# print(yesterday_closing)
# print(todays)
# print(yesterday)
# print(today_closing)
# print(yesterday_closing)


# Mam's way of doing it....

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = float(yesterday_data['4. close'])
before_yesterday_data = data_list[1]
before_yesterday_data = float(before_yesterday_data['4. close'])

diff = (yesterday_closing - before_yesterday_data)
diff_percent = diff / yesterday_closing * 100
if diff_percent >0:
    diff_symbol = '🔺'
else:
    diff_symbol = ' 🔻'

diff_percent = abs(diff_percent)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
print(diff_symbol)
diff_percent = 5
if diff_percent >= 5 :
    response2 = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yesterday}&sortBy=publishedAt&apiKey={api_key}")
    response2.raise_for_status()
    data2 = response2.json()
    news = data2["articles"][:3]
    msg = random.choice(news)
    msg_title = msg['title']
    msg_desc = msg['description']
    proxy_client = TwilioHttpClient()
    client = Client(account_sid , auth_token ,http_client=proxy_client )
    message = client.messages \
        .create(body=
                f'{STOCK} {diff_symbol} {math.floor(diff_percent)}%\nHeadline: {msg_title}\nBrief: {msg_desc}',from_="+15047085982", to="+916263038693")
    print(message.status)

# https://newsapi.org/v2/everything?q={Tesla Inc}&from=2024-01-02&sortBy=publishedAt&apiKey="1a1de6af0f7a47d18e09cbbdc740bb0b"
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

