from flask import Blueprint, request, jsonify
from src.view.http_types.http_request import HttpRequest
from src.main.composer.make_create_juridical_person import make_create_juridical_person
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
        exception_handler = erro_handler(exception)

        return jsonify(exception_handler)