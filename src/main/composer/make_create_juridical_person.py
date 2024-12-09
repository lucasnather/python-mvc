from src.model.repositories.juridical_person_repository import JuridicalPersonRepository
from src.controller.create_juridical_person_controller import CreateJuridicalPersonController
from src.view.create_juridical_person_view import CreateJuridicalPersonView
from src.model.settings.connection import db_connection as DbConnection

def make_create_juridical_person():
    model = JuridicalPersonRepository(DbConnection)
    controller = CreateJuridicalPersonController(model)
    view = CreateJuridicalPersonView(controller)

    return view