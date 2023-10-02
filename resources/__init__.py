from flask import Flask, jsonify
from resources.config import Config
from dotenv import load_dotenv
from flask_smorest import Api
from resources.views import blp as VideoBlueprint
import os
from flask_cors import CORS


def create_app():
    """ 
    Create and configure the Flask application.
    """
    load_dotenv()
    app = Flask(__name__)

    app.config.from_object(Config)
    api = Api(app)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app, resources={r"/*"}, origins="*")

    @app.route("/")
    def hello():
        return jsonify({"greeting": "Hello World"})

    api.register_blueprint(VideoBlueprint)

    # Create the UPLOAD_FOLDER directory if it doesn't exist
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app
