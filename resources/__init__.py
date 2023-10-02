from flask import Flask, jsonify
from resources.config import Config
from dotenv import load_dotenv
from flask_restful import Api
from resources.handles import VideoListResource, VideoToDisk, TranscribeVideo, VideoPlayBack
import os
from flask_cors import CORS

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config.from_object(Config)
    api = Api(app)
    
    CORS(app, resources={r"/*"}, origins="*")
    

    @app.route("/")
    def hello():
        return jsonify({"greeting": "Hello World"})

    api.add_resource(VideoListResource, "/videos")
    api.add_resource(VideoToDisk, "/videos/upload")
    api.add_resource(TranscribeVideo, "/videos/<filename>/transcribe")
    api.add_resource(VideoPlayBack, "/videos/<filename>")

    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app
