from src.model.settings.connection import db_connection as DbConnection
from src.model.repositories.juridical_person_repository import JuridicalPersonRepository
from src.controller.transaction_juridical_person_controller import TransactionNaturalPersonController
from src.view.transaction_juridical_person_view import TransactionJuridicalPersonView

def make_transaction_jurical_person():
    model = JuridicalPersonRepository(DbConnection)
    controller = TransactionNaturalPersonController(model)
    view = TransactionJuridicalPersonView(controller)

    return view