import psycopg2
# from dotenv import load_dotenv
# load_dotenv()
import os

def query_db(query_inserita):
    '''
    Esegue una query inserita come parametro sul db

    Raise Error se la query è fallita
    '''
    try: 
        connection = psycopg2.connect(
            host =      os.getenv("DB_HOST"),
            database =  os.getenv("DB_NAME"),
            user =      os.getenv("DB_USER"),
            password =  os.getenv("DB_PASSWORD"),
            port =      os.getenv("DB_PORT")
        )
        cursor = connection.cursor()
        cursor.execute(query_inserita + " RETURNING id")

        # 2. Recuperiamo l'ID appena inserito (grazie a RETURNING id)
        id_inserito = cursor.fetchone()[0]
        print(f"Rider inserito con successo! ID generato: {id_inserito}")

        # 3. FONDAMENTALE: Conferma e salva l'inserimento nel database reale
        connection.commit()

    except (Exception, psycopg2.Error) as e:
        raise f"Non ti sei connesso a PostgreSQL, {e}"

    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connessione chiusa")