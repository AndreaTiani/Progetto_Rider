import psycopg2

try: 
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )
    cursor = connection.cursor()

    cursor.execute("SELECT version();")

    record = cursor.fetchone()

    print("Ti sei connesso a - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Errore non ti sei conesso a PostgreSQL", error)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connessione chiusa")