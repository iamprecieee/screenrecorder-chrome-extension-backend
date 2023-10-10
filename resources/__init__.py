from dotenv import load_dotenv
from flask import Flask, jsonify
from resources.config import Config
from flask_smorest import Api
from flask_cors import CORS
from resources.views import blp as VideoBlueprint
import models
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """ 
    Create and configure the Flask application.
    """
    load_dotenv()
    app = Flask(__name__)

    app.config.from_object(Config)
    api = Api(app)
    db = SQLAlchemy()
    db.init_app(app)
    migrate = Migrate(app, db)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app, resources={r"/*"}, origins="*")

    @app.route("/")
    def hello():
        return jsonify({"greeting": "Hello World"})

    api.register_blueprint(VideoBlueprint)

    @app.teardown_appcontext
    def close_database(exception):
        """
        This cleans up database-related resources when no longer needed.
        This helps in preventing resource leaks and improving application stability.
        """
        models.storage.close()

    return app
