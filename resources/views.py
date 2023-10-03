from flask_smorest import Blueprint
from resources.utils import generate_unique_filename, get_file_extension, create_video_clip, transcribe_audio
from flask.views import MethodView
import models
from models.model import Video
from flask import jsonify, request, Response
import os
from io import BytesIO
import tempfile
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename


blp = Blueprint("videos", __name__)

unique_name = generate_unique_filename()


@blp.route("/videos")
class VideoList(MethodView):
    def get(self):
        """
        Retrieves a list of video metadata (upload_id and filename included) for uploaded videos.
        """
        try:
            videos = models.storage.all("Video")
            video_list = [{"upload_id": video.id, "filename": video.filename, "extension": video.extension, "size": video.size, "resolution": video.resolution,
                           "created_at": video.created_at}
                          for video in videos]

            return jsonify(video_list), 200

        except Exception as e:
            return jsonify({"error": f"{str(e)}"}), 500


@blp.route("/videos/upload")
class VideoToDisk(MethodView):
    def post(self):
        """
        Uploads and saves a video file to the database.
        """
        content_type = request.headers.get("Content-Type")
        extension = get_file_extension(content_type)

        try:
            video_data = request.data

            if not video_data:
                return jsonify({"error": "Missing video data"}), 400
            if not extension:
                return jsonify({"error": "Unsupported Content-Type"}), 415
            filename = secure_filename(request.headers.get(
                "X-File-Name", f"{unique_name}.{extension}"))

            video = models.storage.getFilename("Video", filename=filename)

            if video:
                chunk_size = 10 * 1024 * 1024  # 10MB chunks
                for chunk in request.stream.read(chunk_size):
                    video_data += chunk
                    models.storage.save()
            else:
                file_size = f"{round(len(video_data) / (1024 * 1024), 2)} mb"
                video_clip = create_video_clip(extension, video_data)
                resolution = f"{video_clip.size[0]} x {video_clip.size[1]}"

                video = Video(filename=filename, data=video_data,
                              size=file_size, resolution=resolution, extension=extension)
                video.save()

            return jsonify({"Uploaded succesfully": f"{filename}", "upload_id": f"{video.id}"}), 201
        except Exception as e:
            return jsonify({"error": f"{str(e)}"}), 500


@blp.route("/videos/<upload_id>")
class VideoPlayBackAndDelete(MethodView):
    def get(self, upload_id):
        """
        Retrieves and serves the requested video for playback.
        """
        video = models.storage.get("Video", id=upload_id)

        if video:
            response = Response(BytesIO(video.data), content_type="video/mp4")
            return response
        else:
            return jsonify({"error": "Video not found"}), 404

    def delete(self, upload_id):
        """ 
        Deletes a specific video from database.
        """
        try:
            video = models.storage.get("Video", id=upload_id)

            if video:
                models.storage.delete("Video", id=video.id)
                models.storage.save()
                return '', 204
            else:
                return jsonify({"error": "Video not found"}), 404

        except Exception as e:
            return jsonify({"error": f"{str(e)}"}), 500


@blp.route("/videos/<upload_id>/transcribe")
class TranscribeVideo(MethodView):
    def get(self, upload_id):
        """
        Transcribes saved video with timestamps.
        """
        video = models.storage.get("Video", id=upload_id)

        if video:
            video_data = BytesIO(video.data)

            if video.filename.endswith(".mp4"):
                file_suffix = ".mp4"
            elif video.filename.endswith(".webm"):
                file_suffix = ".webm"

            with tempfile.NamedTemporaryFile(suffix=file_suffix, delete=False) as temp_video_file:
                temp_video_file.write(video_data.read())
                temp_video_file.seek(0)
                video_clip = VideoFileClip(temp_video_file.name)
                audio_clip = video_clip.audio

                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
                    audio_clip.write_audiofile(temp_audio_file.name)
                transcribed_text = transcribe_audio(temp_audio_file.name)

                # Add timestamp for video length
                duration = int(video_clip.duration)  # seconds
                minutes = duration // 60
                seconds = duration % 60
                timestamp = f"{minutes:02}:{seconds:02}"

                transcribed_with_timestamps = [
                    f"{timestamp} - {transcribed_text}"]

                temp_video_file.close()
                temp_audio_file.close()
                os.remove(temp_video_file.name)
                os.remove(temp_audio_file.name)

            return jsonify({"Transcription": "\n".join(transcribed_with_timestamps)})
        else:
            return jsonify({"error": "Video not found"}), 404
