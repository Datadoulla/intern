import os
from dotenv import load_dotenv

import sqlite3
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Load the stored environment variables
load_dotenv()

# Get the values
env = dict(os.environ)
telegram_key = env['bot_key']

# Fonction pour stocker les données dans la base de données
def stocker_donnees(position, date, link):
    conn = sqlite3.connect('intership.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO application (position, date, link) VALUES (?, ?, ?)''', (position, date, link))
    conn.commit()
    conn.close()

# Fonction pour gérer les messages
def message_handler(update, context):
    message_text = update.message.text
    if ',' in message_text:
        link, position = message_text.split(',', 1)
        date = datetime.now().strftime("%d/%m")
        stocker_donnees(position.strip(), date, link.strip())
        update.message.reply_text("Données enregistrées avec succès !")
    else:
        update.message.reply_text("Format de message incorrect. Utilisez 'lien, position'.")

def main():
    updater = Updater(telegram_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(filters.Filters.text & ~filters.Filters.command, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

