from flask_restful import Resource
from resources.routes import generate_unique_filename, get_file_extension, transcribe_audio
from flask import current_app, jsonify, request, send_from_directory
import os, tempfile
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename


unique_name = generate_unique_filename()

class VideoListResource(Resource):
    """
    Retrieves a list of video metadata (filename, file size, resolution, and extension) for uploaded videos.
    """

    def get(self):
        try:
            video_folder = current_app.config["UPLOAD_FOLDER"]
            video_files = os.listdir(video_folder)
            video_list = []

            for filename in video_files:
                if filename.endswith((".mp4", ".webm", ".mov")):
                    file_path = os.path.join(video_folder, filename)
                    video_clip = VideoFileClip(file_path)

                    video_info = {
                        "file_name": filename,
                        "file_size": f"{round(os.path.getsize(file_path) / (1024 * 1024), 2)} mb",
                        "resolution": f"{video_clip.size[0]} x {video_clip.size[1]}",
                        "extension": os.path.splitext(filename)[1][1:],
                    }

                    video_list.append(video_info)

            return video_list
        except Exception as e:
            return {"error": str(e)}
        
        

class VideoToDisk(Resource):
    """
    Uploads and appends video chunks to an existing video file on the disk.
    """

    def post(self):
        content_type = request.headers.get("Content-Type")
        extension = get_file_extension(content_type)
        try:
            video_data = request.data
            if not video_data:
                return jsonify({"error": "Missing video data"}), 400
            if not extension:
                return jsonify({"error": "Unsupported Content-Type"}), 400
            filename = secure_filename(request.headers.get(
                "X-File-Name", f"{unique_name}.{extension}"))
            file_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"], filename)
            if os.path.exists(file_path):
                with open(file_path, "ab") as f:
                    chunk_size = 10 * 1024 * 1024
                    while True:
                        chunk = request.stream.read(chunk_size)
                        if not chunk:
                            break
                        f.write(chunk)
            else:
                with open(file_path, "wb") as f:
                    f.write(video_data)
            return {"filename": filename}
        except Exception as e:
            return {"error": str(e)}
        
        

class VideoPlayBack(Resource):
    """
    Retrieves and serves the requested video for playback.
    """

    def get(self, filename):
        try:
            return send_from_directory(os.path.join(os.getcwd(), current_app.config["UPLOAD_FOLDER"]), filename)
        except Exception as e:
            return jsonify({"error": str(e)})

        
        
        
class TranscribeVideo(Resource):
    """
    Transcribes saved video with timestamps.
    """

    def get(self, filename):
        try:
            file_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"], filename)
            if not os.path.exists(file_path):
                return jsonify({"error": "Video not found"}), 404
            with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_video_file:
                with open(file_path, "rb") as original_file:
                    temp_video_file.write(original_file.read())
                temp_video_file.seek(0)
                video_clip = VideoFileClip(temp_video_file.name)
                audio_clip = video_clip.audio
                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
                    audio_clip.write_audiofile(temp_audio_file.name)
                transcribed_text = transcribe_audio(temp_audio_file.name)
            return jsonify({"Transcription": transcribed_text})
        except Exception as e:
            return jsonify({"error": str(e)})
