from flask import Blueprint, request, jsonify
from src.view.http_types.http_request import HttpRequest
from src.main.composer.make_create_juridical_person import make_create_juridical_person
from src.main.composer.make_transaction_juridical_person import make_transaction_jurical_person
from src.errors_types.erro_handler import erro_handler

bp_juridical_person = Blueprint("juridical_person", __name__)

@bp_juridical_person.route("/api/juridical", methods=["POST"])
def create():
    try:
        body = request.json

        http_request = HttpRequest(body=body)
        view = make_create_juridical_person()

        http_response = view.handle(http_request=http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = erro_handler(exception)

        return jsonify(http_response.body), http_response.status_code
    
@bp_juridical_person.route("/api/juridical/transaction/<int:juridical_person_id>", methods=["PUT"])
def transaction(juridical_person_id):
    try:
        http_request = HttpRequest(body=request.json, param=juridical_person_id)
        view = make_transaction_jurical_person()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = erro_handler(exception)

        return jsonify(http_response.body), http_response.status_code 
