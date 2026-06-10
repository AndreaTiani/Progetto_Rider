from flask import Blueprint, request, jsonify
# from src.handlers.riders_handler import
# from src.handlers.reviews_handler import
from src.utils import query_db

riders_bp = Blueprint('riders', __name__, url_prefix='/riders')

@riders_bp.route('/test_db', methods=['GET'])
def test_db():
    try:
        query_db("INSERT INTO public.riders (id, name, vehicle, total_deliveries) VALUES (3, 'John Doe', 'Motorcycle', 10)")
        return jsonify({"Message": "Success"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
