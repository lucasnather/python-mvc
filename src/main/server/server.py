from flask import Flask
from flask_cors import CORS
from src.model.settings.connection import db_connection
from src.main.routes.natural_person_routes import bp_natural_person
from src.main.routes.juridical_person_routes import bp_juridical_person

db_connection.connection()
app = Flask(__name__)
CORS(app)

app.register_blueprint(bp_natural_person)
app.register_blueprint(bp_juridical_person)
