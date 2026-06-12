import src.utils as src
import os

# Scrittura
def aggiungi_recensione(query):
    src.db_insert(query)

def popola_tabelle(query):
    src.db_insert(query)
    
def modifica_recensione(query):
    src.db_insert(query)

# Lettura
def elenca_recensioni(query):
    return src.db_select(query)