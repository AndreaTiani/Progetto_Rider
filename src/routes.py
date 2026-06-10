from flask import Blueprint, jsonify, request
import src.handlers.riders_handler as riders_h
import src.handlers.reviews_handler as reviews_h

riders_bp = Blueprint("riders", __name__, url_prefix="/riders")



@riders_bp.route("/create_tables", methods=["POST"])
def create_tables():
    '''
    Inizializza le tabelle del db
    '''
    try:
        riders_h.aggiungi_rider("CREATE TABLE IF NOT EXISTS riders (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name VARCHAR(100) NOT NULL, vehicle VARCHAR(50) NOT NULL, total_deliveries INT NOT NULL DEFAULT 0);")
        riders_h.aggiungi_rider("CREATE TABLE IF NOT EXISTS reviews (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, rider_id INT NOT NULL, customer_name VARCHAR(100) NOT NULL, rating INT NOT NULL, comment VARCHAR(500) DEFAULT NULL, FOREIGN KEY (rider_id) REFERENCES riders(id), CHECK (rating BETWEEN 1 AND 5));")

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500

@riders_bp.route("/insert_table", methods=["POST"])
def insert_table():
    try: 
        riders_h.popola_tabelle("INSERT INTO public.riders (name, vehicle, total_deliveries) VALUES ('Marco Rossi', 'bicycle', 42),('Giulia Bianchi', 'motorcycle', 128),('Luca Ferrari', 'scooter', 77);")
        riders_h.popola_tabelle("INSERT INTO reviews (rider_id, customer_name, rating, comment) VALUES (1, 'Anna Verdi', 5, 'Consegna rapidissima, ottimo!'),(2, 'Paolo Neri', 4, 'Puntuale e cortese.'),(1, 'Sofia Russo', 3, NULL),(3, 'Marco Esposito', 5, 'Perfetto, lo consiglio.'),(2, 'Chiara Conti', 2, 'Un po'' di ritardo.');")
        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500





@riders_bp.route("/test_db", methods=["POST"])
def test_db():
    '''
    Funzione di test per vedere se l'inserimento nel DB funziona
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        riders_h.aggiungi_rider("INSERT INTO public.riders (id, name, vehicle, total_deliveries) VALUES (5, 'John Doe', 'Motorcycle', 10)")
        return jsonify({"Message": "Success, Rider inserito correttamente"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/riders_list", methods=["GET"])
def riders_list():
    '''
    Elenca tutti i corrieri filtrali eventualemente per veicolo, inserire ordinamento da URL???
    Query con SELECT
    Parametro opzionale della funzione "ordina_per"
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata

        vehicle = request.args.get("vehicle")


        """
        Valida il parametro di ordinamento
        colonne_valide = ["id", "name", "vehicle", "total_deliveries"]
        """



        # Costruisce la query SELECT con filtro opzionale per veicolo
        query = "SELECT * FROM riders"
        if vehicle:
            query += f" WHERE vehicle = '{vehicle}'"


        # Passa alla funzione che aprle la connessione al db e esegue la query

        risultato = riders_h.elenca_riders(query)

        return jsonify({"Message": "Success", "data": risultato}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/reviews_add", methods=["POST"])
def reviews_add():
    '''
    Inserisci una recensione, passaggio di parametri tramite BODY e JSON???
    Query con INSERT
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/reviews_update", methods=["PUT"])
def reviews_update():
    '''
    Aggiunge una recensione, passaggio di parametri tramite BODY e JSON???
    Query con MODIFY
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/riders_delete<string:rider_id>", methods=["DELETE"])
def riders_delete():
    '''
    Cancella un rider e tutte le recensioni a lui collegate, inserire id da URL???
    Query con DELETE???
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        
        rider_id = request.args.get("rider_id")

        riders_h.rimuovi_rider(f"DELETE FROM reviews WHERE rider_id = {rider_id};")
        riders_h.rimuovi_rider(f"DELETE FROM riders WHERE id = {rider_id};")


        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/riders_avg", methods=["GET"])
def riders_avg():
    '''
    Fornisce la media dei voti di un rider, inserire i dati da URL???
    Query con SELECT
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500