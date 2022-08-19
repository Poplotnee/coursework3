from flask import Flask
import logging
from error_handler.handlers import error_handlers_blueprint
from main.views import main_blueprint
from api_endpoints.api_views import api_blueprint

app = Flask(__name__)

logging.basicConfig(filename=r"logs\api.log", level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

app.register_blueprint(main_blueprint)
app.register_blueprint(error_handlers_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run()
