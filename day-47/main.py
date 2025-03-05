import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

_TRIGGER_PRICE = 2200.00
load_dotenv()


def send_email(url, product_price, product_name_cleaned):
    receiver_email = os.getenv("EMAIL_ADDRESS", "")
    sender_email = os.getenv("SMTP_ADDRESS", "")
    password = os.getenv("EMAIL_PASSWORD", "")
    email_body = f"{product_name_cleaned} is now ${product_price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=("Subject:Amazon Price Alert!\n\n" + email_body + f"\n{url}").encode(
                "utf-8"
            ),
        )


# url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.com.mx/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
request_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "es;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}
response = requests.get(url, headers=request_headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
price_element = soup.find(name="span", class_="a-offscreen")

if price_element:
    product_price = float(price_element.getText().replace("$", "").replace(",", "").strip())
    product_name_element = soup.find(id="productTitle")
    product_name_cleaned = ""

    if product_name_element:
        product_name = product_name_element.getText()
        product_name_cleaned = " ".join(
            [line.strip() for line in product_name.split("\n")]
        )

    if product_price < _TRIGGER_PRICE:
        send_email(
            url,
            product_price,
            product_name_cleaned,
        )

# In case you get catcha you can follow this steps to skip it https://gist.github.com/TheMuellenator/a5543bd7d8d18dbb8295c3c527fb4cfc?permalink_comment_id=5142250#gistcomment-5142250

