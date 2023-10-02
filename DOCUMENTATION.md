# API Documentation - Video Management API

This documentation provides details about the backend API endpoints for a screenrecorder chrome-extension; which performs operations on the recorded video files including retrieving video metadata, uploading video chunks, serving videos for playback, and transcribing videos with timestamps.

## Base URL

The base URL for all API endpoints is:

**`https://chrome-exx-937e6f500932.herokuapp.com/`**

## Endpoints

### 1. List Videos

#### Retrieve a list of video metadata for uploaded videos.

- **Endpoint URL**: `/videos`
- **HTTP Method**: GET

**Description**: Retrieves a list of video metadata, including filename, file size, resolution, and extension for all uploaded videos.

**Response**:

- Status Code: 200 (OK)

Response Body: An array of video objects, each containing the following properties:
- file_name (string): The name of the video file.
- file_size (string): The file size in megabytes (MB).
- resolution (string): The video resolution (width x height).
- extension (string): The file extension (e.g., "mp4").


- Output:
```json
[
  {
    "file_name": "example.mp4",
    "file_size": "12.34 MB",
    "resolution": "1920 x 1080",
    "extension": "mp4"
  },
  {
    "file_name": "sample.webm",
    "file_size": "8.76 MB",
    "resolution": "1280 x 720",
    "extension": "webm"
  }
]

### 2. Upload Video (Chunks)

#### Uploads and appends video chunks to an existing video file on disk.

- **Endpoint URL**: `/videos/upload`
- **HTTP Method**: POST

**Description**: Retrieves a blob file containing the recorded video and writes the video to a new file/ appends the video in chunks to an existing video file on disk.

**Response**:

- Status Code: 200 (OK)

Response Body: A JSON object containing the uploaded filename:
- file_name (string): The name of the video file.


- Output:
```json
[
  {
    "file_name": "example.mp4"
  },
  {
    "file_name": "sample.webm"
  }
]


### 3. Retrieve Video for Playback

#### Retrieves and serves the requested video for playback.

- **Endpoint URL**: `/videos/<filename>`
- **HTTP Method**: GET
- **Path Parameter**: filename (string): The name of the video file to retrieve.

**Description**: Retrieves and serves the requested video for playback.

**Response**:

- Status Code: 200 (OK)

Response Body: The video file for playback.


- Output: The video File


### 4. Transcribe Video with Timestamps

#### Transcribes a saved video with timestamps.

- **Endpoint URL**: `/videos/<filename>/transcribe`
- **HTTP Method**: GET
- **Path Parameter**: filename (string): The name of the video file to retrieve.

**Description**: Transcribes a saved video with timestamps.

**Response**:

- Status Code: 200 (OK)

Response Body: A JSON object containing the transcribed text with timestamps.


- Output:
```json
[
  {
    "Transcription": "00: you"
  }
]


