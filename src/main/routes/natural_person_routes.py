from flask import Blueprint, request, jsonify
from src.main.composer.make_create_natural_person import make_create_natural_person
from src.main.composer.make_transaction_natural_person import make_transaction_natural_person
from src.view.http_types.http_request import HttpRequest
from src.errors_types.erro_handler import erro_handler

bp_natural_person = Blueprint("natural_person", __name__)

@bp_natural_person.route("/api/natural", methods=["POST"])
def create():
    print("rcebi")
    try:
        http_request = HttpRequest(body=request.json)
        view = make_create_natural_person()

        http_response = view.handle(http_request)

        print(http_response)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = erro_handler(exception)

        return jsonify(http_response.body), http_response.status_code
    
@bp_natural_person.route("/api/natural/transaction/<int:natural_person_id>", methods=["PUT"])
def transaction(natural_person_id):
    try:
        http_request = HttpRequest(body=request.json, param=natural_person_id)
        view = make_transaction_natural_person()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = erro_handler(exception)

        return jsonify(http_response.body), http_response.status_code 

       
   