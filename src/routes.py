from flask import Blueprint, request, jsonify

rider_bp = Blueprint('rider', __name__, url_prefix='/rider')