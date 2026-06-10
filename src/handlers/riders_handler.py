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

def elenca_riders(query):
    try:
        return src.db_select(query)
    except:
        raise