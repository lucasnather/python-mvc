from src.model.settings.connection import db_connection as DbConnection
from src.model.repositories.natural_person_repository import NaturalPersonRepository
from src.controller.transaction_natural_person_controller import TransactionNaturalPersonController
from src.view.transaction_natural_person_view import TransactionNaturalPersonView

def make_transaction_natural_person():
    model = NaturalPersonRepository(DbConnection)
    controller = TransactionNaturalPersonController(model)
    view = TransactionNaturalPersonView(controller)

    return view