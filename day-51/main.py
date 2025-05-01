import os
from dotenv import load_dotenv
from internet_speed_twitter_bot import InternetSpeedTwitterBot
from internet_speed_twitter_bot import Config


load_dotenv()

config = Config(
    twitter_email=os.getenv("TWITTER_EMAIL", ""),
    twitter_password=os.getenv("TWITTER_PASSWORD", ""),
    chrome_driver_path=os.getenv("CHROME_DRIVER_PATH", ""),
    promised_down=int(os.getenv("PROMISED_DOWN", 0)),
    primised_up=int(os.getenv("PRIMISED_UP", 0)),
)


internet_speed_bot = InternetSpeedTwitterBot(config)
internet_speed_bot.get_internet_speed()
internet_speed_bot.tweet_at_provider()
