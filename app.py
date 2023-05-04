from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler,Filters
from main import start, echo



app = Flask(__name__)
TOKEN = '5925963662:AAEV877ngAyEkhmJE-rLw6536m2JqnQzJlc'

bot: Bot = Bot(TOKEN)


@app.route('/bot', methods=['POST', 'GET'])
def webhookbot():

    if request.method == 'GET':
        return 'webhook is working!'

    elif request.method == 'POST':
        data = request.get_json()

        dp = Dispatcher(bot, None, workers=0)

        # create update obj
        update: Update = Update.de_json(data, bot)

        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(MessageHandler(Filters.all,echo))

        # process update
        dp.process_update(update)

        return {"status": 200}
    
if __name__=='__main__':
    app.run(debug=True)