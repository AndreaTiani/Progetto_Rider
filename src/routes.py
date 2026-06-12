from flask import Blueprint, jsonify, request
import src.handlers.riders_handler as riders_h
import src.handlers.reviews_handler as reviews_h

riders_bp = Blueprint("riders", __name__, url_prefix="/riders")


@riders_bp.route("/create_tables", methods=["POST"])
def create_tables():
    '''
    Inizializza le tabelle del db

    Imposta vincoli di attributo e di chiave esterna
    '''
    try:
        riders_h.crea_tabella("CREATE TABLE IF NOT EXISTS riders (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name VARCHAR(100) NOT NULL, vehicle VARCHAR(50) NOT NULL, total_deliveries INT NOT NULL DEFAULT 0);")
        riders_h.crea_tabella("CREATE TABLE IF NOT EXISTS reviews (id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, rider_id INT NOT NULL, customer_name VARCHAR(100) NOT NULL, rating INT NOT NULL, comment VARCHAR(500) DEFAULT NULL, FOREIGN KEY (rider_id) REFERENCES riders(id), CHECK (rating BETWEEN 1 AND 5));")

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500



@riders_bp.route("/fill_tables", methods=["POST"])
def fill_tables():
    '''
    Inserisce dei valori di default nelle tabelle
    '''
    try:
        riders_h.popola_tabelle("INSERT INTO riders (name, vehicle, total_deliveries) VALUES ('Marco Rossi', 'bicycle', 42), ('Giulia Bianchi', 'motorcycle', 128),('Luca Ferrari', 'scooter', 77);")
        reviews_h.popola_tabelle("INSERT INTO reviews (rider_id, customer_name, rating, comment) VALUES (1, 'Anna Verdi', 5, 'Consegna rapidissima, ottimo!'),(2, 'Paolo Neri', 4, 'Puntuale e cortese.'),(1, 'Sofia Russo', 3, NULL),(3, 'Marco Esposito', 5, 'Perfetto, lo consiglio.'),(2, 'Chiara Conti', 2, 'Un po'' di ritardo.');")
        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500



@riders_bp.route("/riders_list", methods=["GET"])
def riders_list():
    '''
    Elenca tutti i riders filtrati eventualemente per veicolo
    '''
    try:
        vehicle = request.args.get("vehicle")

        # Costruisce la query SELECT con filtro opzionale per veicolo
        query = "SELECT * FROM riders"
        if vehicle:
            query += f" WHERE vehicle = '{vehicle}'"

        risultato = riders_h.elenca_riders(query)
        return jsonify({"Message": "Success", "data": risultato}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500



@riders_bp.route("/riders_avg/<string:rider_id>", methods=["GET"])
def riders_avg(rider_id):
    '''
    Fornisce la media dei rating di un rider
    '''
    try:
        risultato = riders_h.media_rider(f"SELECT rider_id, AVG(rating) FROM reviews GROUP BY rider_id HAVING rider_id = {rider_id}")

        return jsonify({"Message": "Success", "Data": risultato}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500



@riders_bp.route("/riders_delete/<string:rider_id>", methods=["DELETE"])
def riders_delete(rider_id):
    '''
    Cancella un rider e tutte le recensioni a lui collegate
    '''
    try:
        riders_h.rimuovi_rider(f"DELETE FROM reviews WHERE rider_id = {rider_id};")
        riders_h.rimuovi_rider(f"DELETE FROM riders WHERE id = {rider_id};")

        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500



@riders_bp.route("/reviews_list", methods=["GET"])
def reviews_list():
    '''
    Elenca tutti le reviews filtrate eventualemente per rating
    '''
    try:
        rating = request.args.get("rating")

        # Costruisce la query SELECT con filtro opzionale per veicolo
        query = "SELECT * FROM reviews"
        if rating:
            query += f" WHERE rating = {rating}"

        risultato = reviews_h.elenca_recensioni(query)
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
    Aggiunde una recensione al db
    '''
    try:
        data = request.get_json()

        rider_id      = data["rider_id"]
        customer_name = data["customer_name"]
        rating        = data["rating"]
        comment       = data["comment"] or None

        if not rider_id or not customer_name or not rating:
            raise ValueError("rider_id, customer_name e rating sono obbligatori")

        reviews_h.aggiungi_recensione(f"INSERT INTO reviews (rider_id, customer_name, rating, comment) VALUES ({rider_id}, '{customer_name}', {rating}, '{comment}')")
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
    Modifica una recensione nel db
    '''
    try:
        data = request.get_json()

        review_id =     data["id"]
        rider_id =      data["rider_id"]
        customer_name = data["customer_name"]
        rating =        data["rating"]
        comment =       data["comment"] or None

        if not rider_id or not customer_name or not rating or not rating:
            raise ValueError("rider_id, review_id, customer_name e rating sono obbligatori")

        reviews_h.modifica_recensione(f"UPDATE reviews SET rider_id = {rider_id}, customer_name = '{customer_name}', rating = {rating}, comment = '{comment}' WHERE id = {review_id}")
        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500



@riders_bp.route("/drop_tables", methods=["DELETE"])
def drop_tables():
    '''
    Cancella le tabelle e i loro dati dal db
    '''
    try:
        riders_h.droppa_tabella("DROP TABLE IF EXISTS reviews")
        riders_h.droppa_tabella("DROP TABLE IF EXISTS riders")
        return jsonify({"Message": "Success"}), 200

    except RuntimeError as e:
        return jsonify({"Error": "Database non raggiungibile, " + str(e)}), 500

    except ValueError as e:
        return jsonify({"Error": "Impossibile eseguire la query, " + str(e)}), 400

    except Exception as e:
        return jsonify({"Error": "Errore imprevisto, " + str(e)}), 500