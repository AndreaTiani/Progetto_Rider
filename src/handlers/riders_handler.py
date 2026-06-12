import src.utils as src
import os

# Scrittura
def crea_tabella(query):
    src.db_insert(query)

def aggiungi_rider(query):
    src.db_insert(query)

def popola_tabelle(query):
    src.db_insert(query)

def rimuovi_rider(query):
    src.db_insert(query)

def droppa_tabella(query):
    src.db_insert(query)

# Lettura
def elenca_riders(query):
    return src.db_select(query)

def media_rider(query):
    return src.db_select(query)