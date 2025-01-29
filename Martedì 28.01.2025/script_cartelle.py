import os
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, "it_IT.utf8")

directory_destinazione = "cartelle_date"

if not os.path.exists(directory_destinazione):
    os.makedirs(directory_destinazione)


start_date = datetime(2025, 1, 29)
end_date = datetime(2025, 3, 1)


current_date = start_date
while current_date <= end_date:
    if current_date.weekday() not in (5, 6):

        nome_cartella = current_date.strftime("%d-%m-%Y - %A")
        percorso_cartella = os.path.join(directory_destinazione, nome_cartella)
        os.makedirs(percorso_cartella, exist_ok=True)
        print(f"Creata cartella: {percorso_cartella}")

    current_date += timedelta(days=1)

print("Tutte le cartelle sono state create correttamente.")
