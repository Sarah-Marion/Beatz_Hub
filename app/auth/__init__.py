from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import error, forms, views