import src.utils as src
import os

def aggiungi_recensioni(query):
    try:
        src.db_insert(query)
    except:
        raise

def popola_tabelle(query):
    try:
        src.db_insert(query)
    except:
        raise
    
def modifica_recensione(query):
    try:
        src.db_insert(query)
    except:
        raise