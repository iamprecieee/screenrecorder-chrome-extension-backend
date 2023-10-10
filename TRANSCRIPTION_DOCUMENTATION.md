# API Documentation - Video Transcription

This documentation provides details about the API endpoint for the chrome-extension backend which performs operations for transcribing videos with timestamp of video duration.

## Description

The video file is converted to an audio file, which is then transcribed to text using openAI's [Whisper](https://github.com/openai/whisper). The transcript output is saved to the database.

## Base URL

The base URL for all API endpoints is:

**`https://chrome-exx-937e6f500932.herokuapp.com/`**

## Endpoints

### 4. Transcribe Video with Timestamp

#### Transcribes a saved video with timestamp.

- **Endpoint URL**: `/videos/<filename>/transcribe`
- **HTTP Method**: POST
- **Path Parameter**: filename (string): The name of the video file to transcribe.

**Description**: Transcribes a saved video with timestamp of video duration.

**Response**:

- Status Code: 200 (OK)

- Output:
```json
[
  {
    "message": "Video transcribed successfully"
  }
]

#### Retrieves the transcript of a saved video with timestamp.

- **Endpoint URL**: `/videos/<filename>/transcribe`
- **HTTP Method**: GET
- **Path Parameter**: filename (string): The name of the video file to retrieve its transcript.

**Description**: Retrieves the transcript of a saved video with timestamp of video duration.

**Response**:

- Status Code: 200 (OK)

- Response Body: A JSON object containing the transcribed text with timestamp.


- Output:
```json
[
  {
    "Transcription": "00:05 - This is a transcript sample."
  }
]

