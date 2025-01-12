import os


bot_token = os.getenv('BOT_TOKEN')

admin_list = map(int, os.getenv('ADMINS').split())
