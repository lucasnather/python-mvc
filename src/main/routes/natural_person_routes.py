from flask import Blueprint, request, jsonify
from src.main.composer.make_create_natural_person import make_create_natural_person
from src.view.http_types.http_request import HttpRequest

bp_natural_person = Blueprint("natural_person", __name__)

@bp_natural_person.route("/api/natural", methods=["POST"])
def create():
    try:
        http_request = HttpRequest(body=request.json)
        view = make_create_natural_person()

        http_response = view.handle(http_request)

        print(http_response)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        print(exception)
        return jsonify({
            "message": "Erro"
        })
       
   