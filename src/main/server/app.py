from flask import Flask
from src.model.settings.connection import db_connection

app = Flask(__name__)

db_connection.connection()