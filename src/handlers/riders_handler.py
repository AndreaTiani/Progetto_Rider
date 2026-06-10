import src.utils as src
import os

def aggiungi_rider(query):
    try:
        src.db_insert(query)
    except:
        raise

def popola_tabelle(query):
    try:
        src.db_insert(query)
    except:
        raise