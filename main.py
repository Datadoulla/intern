import os
import sqlite3
#from dotenv import load_dotenv
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from database_setup import create_tables

# Charger les variables d'environnement
#load_dotenv()

# Récupérer les valeurs des variables d'environnement
telegram_key = os.getenv('bot_key')

create_tables()

# Fonction pour stocker les données dans la table 'application' de la base de données 'intership.db'
def store_application_data(position, date, link, company):
    conn = sqlite3.connect('intership.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO application (position, date, link, compagny) VALUES (?, ?, ?, ?)''', 
                   (position, date, link, company))
    conn.commit()
    conn.close()

# Fonction pour stocker les données dans la table 'update' de la base de données 'intership.db'
def store_update_data(link, entretien, date_ent):
    conn = sqlite3.connect('intership.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO updatet (link, entretien, date_ent) VALUES (?, ?, ?)''', 
                   (link, entretien, date_ent))
    conn.commit()
    conn.close()

# Fonction pour gérer la commande /addapplication
def add_application(update: Update, context: CallbackContext):
    args = context.args
    if len(args) >= 3:
        link, position, company = args[:3]
        date = datetime.now().strftime("%d/%m")
        store_application_data(position.strip(), date, link.strip(), company.strip())
        update.message.reply_text("Data stored successfully!")
    else:
        update.message.reply_text("Incorrect command format. Use '/addapplication link position company'.")

# Fonction pour gérer la commande /updateapplication
def update_application(update: Update, context: CallbackContext):
    original_message_text = update.message.reply_to_message.text
    # Récupérer le lien à partir du message original
    link = original_message_text.split()[1] if original_message_text else None
    args = context.args
    if len(args) >= 2:
        entretien = args[0]
        date_ent = args[1] if len(args) == 2 else None
        store_update_data(link.strip(), entretien.strip(), date_ent.strip() if date_ent else None)
        update.message.reply_text("Data stored successfully!")
    else:
        update.message.reply_text("Incorrect command format. Use '/updateapplication link entretien [date_ent]'.")

def main():
    updater = Updater(telegram_key, use_context=True)
    dp = updater.dispatcher

    # Ajouter les gestionnaires de commande pour /addapplication et /updateapplication
    dp.add_handler(CommandHandler("addapplication", add_application))
    dp.add_handler(CommandHandler("updateapplication", update_application))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
