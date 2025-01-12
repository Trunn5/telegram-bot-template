import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

admin_list = map(int, os.getenv('ADMINS').split())
