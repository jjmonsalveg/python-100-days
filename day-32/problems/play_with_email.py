# see: https://www.udemy.com/course/100-days-of-code/learn/lecture/21712834?start=1#overview
# By default smtplib.SMTP uses port 25. This used to be the standard SMTP port, but because of abuse in the past most servers nowadays have blocked this port to external traffic. There are still some that do allow it; Hotmail, Live, etc. Port 25 is still used for traffic between servers, but many providers have switched to using port 587 for external traffic. If in doubt, search the internet for "smtp server settings" for your provider.

# Add a port number by changing your code to this:

# smtplib.SMTP("smtp.gmail.com", port=587)
# hotmail: smtp.live.com, yahoo: smtp.mail.yahoo.com

import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD_SENDER")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="dowirav302@cpaurl.com", msg="Subject:Hello\n\nThis is the body of my email.")