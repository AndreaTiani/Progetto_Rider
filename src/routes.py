from flask import Blueprint, jsonify, request
import src.handlers.riders_handler as riders_h
import src.handlers.reviews_handler as reviews_h

riders_bp = Blueprint("riders", __name__, url_prefix="/riders")

#TODO
# 1. Gestione ID autoincrementale per le entità
# 2. Gestione dei vincoli di attributo come: 
#       rating compreso tra 1 e 5
#       total_deliveries che parte da 0
#       comment è facoltativo ,,,,

@riders_bp.route("/create_tables", methods=["POST"])
def create_tables():
    '''
    Inizializza le tabelle del db e le popola con i valori di default
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        riders_h.aggiungi_rider("CREATE TABLE IF NOT EXISTS riders (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name VARCHAR(100) NOT NULL, vehicle VARCHAR(50) NOT NULL, total_deliveries INT NOT NULL DEFAULT 0);")
        riders_h.aggiungi_rider("CREATE TABLE IF NOT EXISTS reviews (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, rider_id INT NOT NULL, customer_name VARCHAR(100) NOT NULL, rating INT NOT NULL, comment VARCHAR(500) DEFAULT NULL, FOREIGN KEY (rider_id) REFERENCES riders(id), CHECK (rating BETWEEN 1 AND 5));")

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500

@riders_bp.route("/fill_tables", methods=["POST"])
def fill_tables():
    try:
        riders_h.popola_tabelle("INSERT INTO public.riders (name, vehicle, total_deliveries) VALUES ('Marco Rossi', 'bicycle', 42), ('Giulia Bianchi', 'motorcycle', 128),('Luca Ferrari', 'scooter', 77);")
        reviews_h.popola_tabelle("INSERT INTO public.reviews (rider_id, customer_name, rating, comment) VALUES (1, 'Anna Verdi', 5, 'Consegna rapidissima, ottimo!'),(2, 'Paolo Neri', 4, 'Puntuale e cortese.'),(1, 'Sofia Russo', 3, NULL),(3, 'Marco Esposito', 5, 'Perfetto, lo consiglio.'),(2, 'Chiara Conti', 2, 'Un po'' di ritardo.');")
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
    try:
        data = request.get_json()

        rider_id      = data["rider_id"]
        customer_name = data["customer_name"]
        rating        = data["rating"]
        comment       = data["comment"]

        if not rider_id or not customer_name:
            raise ValueError("rider_id e customer_name sono obbligatori")
        if not (1 <= int(rating) <= 5):
            raise ValueError("rating deve essere tra 1 e 5")

        reviews_h.aggiungi_recensioni(f"INSERT INTO public.reviews (rider_id, customer_name, rating, comment) VALUES ({rider_id}, '{customer_name}', {rating}, '{comment}')")
        '''
        Inserisci una recensione, passaggio di parametri tramite BODY e JSON???
        Query con INSERT
        '''
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
        # 
        data = request.get_json()

        if not data:
            raise ValueError("Body della richiesta mancante o non valido")

        # Estraggo i parametri necessari dal JSON
        review_id = data.get("id")
        rider_id = data.get("rider_id")
        customer_name = data.get("customer_name")
        rating = data.get("rating")
        comment = data.get("comment")   

        # Controllo campi parametri
        if not review_id:
            raise ValueError("Campo 'id' obbligatorio")
        if not rider_id:
            raise ValueError("Campo 'rider_id' obbligatorio")
        if not customer_name:
            raise ValueError("Campo 'customer_name' obbligatorio")
        if not rating:
            raise ValueError("Campo 'rating' obbligatorio")
        
        # Costruzione della query di UPDATE
        query = f"UPDATE reviews SET rider_id = {rider_id}, customer_name = '{customer_name}', rating = {rating}, comment = '{comment}' WHERE id = {review_id}"


        # Passa alla funzione che apre la connessione al db e esegue la query
        reviews_h.modifica_recensione(query)

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/riders_delete/<string:rider_id>", methods=["DELETE"])
def riders_delete(rider_id):
    '''
    Cancella un rider e tutte le recensioni a lui collegate, inserire id da URL???
    Query con DELETE???
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        
        # rider_id = request.args.get("rider_id")

        riders_h.rimuovi_rider(f"DELETE FROM reviews WHERE rider_id = {rider_id};")
        riders_h.rimuovi_rider(f"DELETE FROM riders WHERE id = {rider_id};")


        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500


@riders_bp.route("/riders_avg/<string:rider_id>", methods=["GET"])
def riders_avg(rider_id):

    risultato = riders_h.media_rider(f"SELECT rider_id, AVG(rating) FROM reviews GROUP BY rider_id HAVING rider_id = {rider_id}")

    '''
    Fornisce la media dei voti di un rider, inserire i dati da URL???
    Query con SELECT
    '''
    try:
        # Esegui la query usando la nuova funzione query_db strutturata
        

        return jsonify({"Message": "Success", "Data": risultato}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500