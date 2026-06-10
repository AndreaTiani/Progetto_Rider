import src.utils
import os

def aggiungi_recensioni(query):
    try:
        return src.db_select(query)
    except:
        raise