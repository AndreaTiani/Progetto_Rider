import src.utils
import os

CSV_PATH = os.getenv("CSV_PATH", "PATH error")

def leggi_prodotti():
    try:
        file = open(CSV_PATH, mode='r', encoding='utf-8')
        list_prodotti = []
        valore = file.readline()
        valore = file.readline()    # Salta intestazione

        while valore != "":
            list_prodotti.append(valore.strip())
            valore = file.readline()
        file.close()
        
        dict_prodotti = [{"name":i.split(',')[0], "quantity": int(i.split(',')[1]), "category": i.split(',')[2]} for i in list_prodotti]
        return dict_prodotti
    except FileNotFoundError:
        raise FileNotFoundError("File 'products.csv' not found")


def crea_prodotti(json_prodotti):
    try:
        csv_prodotti = leggi_prodotti()
        chiavi_csv = [i["name"] for i in csv_prodotti]
        chiavi_json = [i["name"] for i in json_prodotti]

        for i in chiavi_json:
            if i in chiavi_csv:
                raise FileNotFoundError(f"Product {i} already exists") 

        file = open(CSV_PATH, mode='a', encoding='utf-8')
        for item in json_prodotti:
            riga_csv = f"{item["name"]},{item["quantity"]},{item["category"]}\n"
            file.write(riga_csv)
        file.close()
    except:
        raise


def aggiorna_prodotti(json_prodotti):
    try:
        csv_prodotti = leggi_prodotti()
        chiavi_csv = [i["name"] for i in csv_prodotti]
        chiavi_json = [i["name"] for i in json_prodotti]

        for i in chiavi_json:
            if i not in chiavi_csv:
                raise FileNotFoundError(f"Product '{i}' not found") 

        for i in csv_prodotti:
            for j in json_prodotti:
                if j["name"] == i["name"]:
                    i["quantity"] = int(j["quantity"])
                    i["category"] = j["category"]

        file = open(CSV_PATH, mode='w', encoding='utf-8')
        file.write("name,quantity,category\n")
        for item in csv_prodotti:
            riga_csv = f"{item["name"]},{item["quantity"]},{item["category"]}\n"
            file.write(riga_csv)
        file.close()
    except:
        raise


def cancella_prodotti(nomi_separati):
    try:
        print(nomi_separati)
        csv_prodotti = leggi_prodotti()
        chiavi_csv = [i["name"] for i in csv_prodotti]
        chiavi_nomi_separati = nomi_separati.split(',')

        for i in chiavi_nomi_separati:
            if i not in chiavi_csv:
                raise FileNotFoundError(f"Product '{i}' not found")

        csv_aggiornato = [item for item in csv_prodotti if item["name"] not in chiavi_nomi_separati]

        file = open(CSV_PATH, mode='w', encoding='utf-8')
        file.write("name,quantity,category\n")
        for item in csv_aggiornato:
            riga_csv = f"{item["name"]},{item["quantity"]},{item["category"]}\n"
            file.write(riga_csv)
        file.close()
    except:
        raise


def conta_prodotti(categoria=None):
    try:
        prodotti = leggi_prodotti()
        quantita = 0
        if categoria == None:
            for i in prodotti:
                quantita += i["quantity"]
            return quantita
        else:
            for i in prodotti:
                if i["category"] == categoria:
                    quantita += i["quantity"]
            return quantita
    except:
        raise