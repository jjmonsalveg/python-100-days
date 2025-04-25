import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

_ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
_NEWS_API_KEY = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone_number = os.getenv("TWILIO_FROM_NUMBER")
to_phone_number = os.getenv("TWILIO_TO_NUMBER")

UP_ICON = "🔺"
DOWN_ICON = "🔻"

stock_price_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={_ALPHAVANTAGE_API_KEY}"
r = requests.get(stock_price_url)

data = r.json()["Time Series (Daily)"]
last_two_days_keys = list(data.keys())[:2]
yesterday_close_key = last_two_days_keys[0]
before_yesterday_close_key = last_two_days_keys[1]

yesterday_close = float(data[yesterday_close_key]["4. close"])
before_yesterday_close = float(data[before_yesterday_close_key]["4. close"])
percentage = (yesterday_close - before_yesterday_close) / before_yesterday_close

if abs(percentage) >= 0.05:
    parameters = {
        "q": COMPANY_NAME,
        "from": yesterday_close_key,
        "to": yesterday_close_key,
        "sortBy": "publishedAt:asc",
        "apiKey": _NEWS_API_KEY,
        "pageSize": 3,
    }

    news_url = "https://newsapi.org/v2/everything"
    articles = requests.get(news_url, params=parameters).json()["articles"]

    for article in articles[:3]:
        selected_icon = UP_ICON if percentage > 0 else DOWN_ICON
        msg = (
            f"TSLA: {selected_icon}{abs(percentage * 100):.2f}%\nHeadline:{article['title']}\n"
            + f"Brief: {article['description']}"
        )
        print(msg)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=to_phone_number, from_=from_phone_number, body=msg
        )

        print(message.sid)
        print(message.status)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
