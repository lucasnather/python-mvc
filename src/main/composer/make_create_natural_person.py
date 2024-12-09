from src.model.repositories.natural_person_repository import NaturalPersonRepository
from src.model.settings.connection import db_connection as DbConnection
from src.controller.create_natural_person_controller import CreateNaturalPersonController
from src.view.create_natural_person_view import CreateNaturalPersonView

def make_create_natural_person():
    model = NaturalPersonRepository(DbConnection)
    controller = CreateNaturalPersonController(model)
    view = CreateNaturalPersonView(controller)

    return view