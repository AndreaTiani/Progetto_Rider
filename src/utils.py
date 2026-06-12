import os
import psycopg2
from psycopg2 import OperationalError, ProgrammingError, DatabaseError


def db_insert(query_inserita):
    """
    Esegue una query inserita come parametro sul db
    Solleva un'eccezione specifica a seconda del tipo di fallimento
    Non ha valori di ritorno
    """

    connection = None
    cursor = None

    # 1. TENTATIVO DI CONNESSIONE
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )
        cursor = connection.cursor()

    except OperationalError as e:
        raise RuntimeError(f"Errore di CONNESSIONE al database: {e}") from e

    # 2. TENTATIVO DI ESECUZIONE QUERY
    try:
        cursor.execute(query_inserita)
        connection.commit()

    except (ProgrammingError, DatabaseError) as e:
        if connection:
            connection.rollback()
        raise ValueError(f"Errore di ESECUZIONE della query: {e}") from e

    except Exception as e:
        if connection:
            connection.rollback()
        raise RuntimeError(f"Errore generico durante l'operazione: {e}") from e

    # 3. CHIUSURA RISORSE
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("PostgreSQL connessione chiusa")



def db_select(query_inserita):
    """
    Esegue una query inserita come parametro sul db
    Solleva un'eccezione specifica a seconda del tipo di fallimento
    Ha valori di ritorno
    """

    connection = None
    cursor = None

    # 1. TENTATIVO DI CONNESSIONE
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )
        cursor = connection.cursor()

    except OperationalError as e:
        raise RuntimeError(f"Errore di CONNESSIONE al database: {e}") from e

    # 2. TENTATIVO DI ESECUZIONE QUERY
    try:
        cursor.execute(query_inserita)
        connection.commit()
        risultato = cursor.fetchall()
        return risultato

    except (ProgrammingError, DatabaseError) as e:
        if connection:
            connection.rollback()
        raise ValueError(f"Errore di ESECUZIONE della query: {e}") from e

    except Exception as e:
        if connection:
            connection.rollback()
        raise RuntimeError(f"Errore generico durante l'operazione: {e}") from e

    # 3. CHIUSURA RISORSE
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("PostgreSQL connessione chiusa")