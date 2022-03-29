from flask import Flask

from src.allocation.config import config
from src.allocation.entrypoints.route import app_route

app = Flask(__name__)

app.register_blueprint(app_route)


app.run(*config.server_config())
