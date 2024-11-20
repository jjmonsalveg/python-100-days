import smtplib
import pandas as pd
from datetime import datetime as dt
import random
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD_SENDER")

data_birthdays = pd.read_csv("birthdays.csv")
today = dt.now()

# or you can do data.iterrows() and use dict compresion to build a dict
todays_birthdays = data_birthdays[(data_birthdays.month == today.month) & (data_birthdays.day == today.day)]

with open (f"letter_templates/letter_{random.randint(1,3)}.txt") as file_letter:
    letter_msg = file_letter.read()

for row in todays_birthdays.to_dict(orient="records"):
   email_body = letter_msg.replace('[NAME]', row["name"])
   
   with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=row["email"],
            msg="Subject:Happy Birthday!\n\n"+email_body,
    )




