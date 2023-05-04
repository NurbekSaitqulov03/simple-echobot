from telegram import Bot
import os
import requests

TOKEN = os.environ.get('TOKEN')

bot = Bot(TOKEN)

url = 'https://nurbeksaitqulov23.pythonanywhere.com/bot'

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook", params={'url':url})
r = requests.get(f"https://api.telegram.org/bot{TOKEN}/GetWebhookInfo", params={'url':url})

print(r.json())