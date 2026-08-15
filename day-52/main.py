import os
from dotenv import load_dotenv
from follower_instagram_bot import FollowerInstagramBot
from follower_instagram_bot import Config


load_dotenv()

config = Config(
    instagram_email=os.getenv("INSTAGRAM_EMAIL", ""),
    instagram_password=os.getenv("INSTAGRAM_PASSWORD", ""),
    similar_account=os.getenv("SIMILAR_ACCOUNT", ""),
)

instagram_bot = FollowerInstagramBot(config)
instagram_bot.login_provider()
instagram_bot.find_followers()
instagram_bot.follow()
