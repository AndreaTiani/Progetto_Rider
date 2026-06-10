from flask import Blueprint, jsonify, request
import src.handlers.riders_handler as riders_h
import src.handlers.reviews_handler as reviews_h

riders_bp = Blueprint("riders", __name__, url_prefix="/riders")

#TODO
# 1. Gestione ID autoincrementale per le entità
# 2. Gestione dei vincoli di attributo come: 
#       rating compreso tra 1 e 5
#       total_deliveries che parte da 0
#       comment è facoltativo

@riders_bp.route("/create_tables", methods=["POST"])
def create_tables():
    '''
    Inizializza le tabelle del db e le popola con i valori di default
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
    Elenca tutti i corriere filtrati eventualemente per veicolo, inserire ordinamento da URL???
    Query con SELECT
    Parametro opzionale della funzione "ordina_per"
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


@riders_bp.route("/riders_delete", methods=["DELETE"])
def riders_delete():
    '''
    Cancella un rider e tutte le recensioni a lui collegate, inserire id da URL???
    Query con DELETE???
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