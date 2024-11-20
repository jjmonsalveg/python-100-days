
import datetime as dt
import smtplib
import random

_DAYS_OF_WEEK = ("Monday", "Tuesday", "Wenesday", "Thursday","Friday","Saturday", "Sunday")
_MY_EMAIL = "giraldojose1996@gmail.com"
_PASSWORD = "mwwh pwui dsbm izxz"

now = dt.datetime.now()
day_of_week = _DAYS_OF_WEEK[now.weekday()]

with open("quotes.txt", mode="r") as quote_file:
   quotes = quote_file.readlines() 

selected_quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=_MY_EMAIL, password=_PASSWORD)
    connection.sendmail(
        from_addr=_MY_EMAIL,
        to_addrs="samoc23705@anypng.com",
        msg=f"Subject:Happy {day_of_week}\n\n {selected_quote}",
    )