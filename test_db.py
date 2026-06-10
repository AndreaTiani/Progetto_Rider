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

    query_test = "INSERT INTO public.riders (id, name, vehicle, total_deliveries) VALUES (2, 'John Doe', 'Motorcycle', 10) RETURNING id;"
    cursor.execute(query_test)

    # 2. Recuperiamo l'ID appena inserito (grazie a RETURNING id)
    id_inserito = cursor.fetchone()[0]
    print(f"Rider inserito con successo! ID generato: {id_inserito}")

    # 3. FONDAMENTALE: Conferma e salva l'inserimento nel database reale
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Errore non ti sei connesso a PostgreSQL", error)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connessione chiusa")