import src.utils as src
import os

def aggiungi_rider(query):
    try:
        src.db_insert(query)
    except:
        raise



def elenca_riders(query):
    return src.db_select(query)