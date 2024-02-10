import os
import sqlite3

# Fonction pour créer les tables si elles n'existent pas
def create_tables():
    # Vérifier si le fichier de base de données existe
    if not os.path.exists('intership.db'):
        print("La base de données 'intership.db' n'existe pas. Création de la base de données...")
    conn = sqlite3.connect('intership.db')
    cursor = conn.cursor()
    # Vérifier si la table 'application' existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS application (
                        position TEXT,
                        date TEXT,
                        link TEXT,
                        compagny TEXT
                    )''')
    # Vérifier si la table 'update' existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS updatet (
                        link TEXT,
                        entretien TEXT,
                        date_ent TEXT
                    )''')
    conn.commit()
    conn.close()

# Appeler la fonction pour créer les tables si ce fichier est exécuté comme un script
if __name__ == "__main__":
    create_tables()
