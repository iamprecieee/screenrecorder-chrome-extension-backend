# API Documentation - Video Transcription

This documentation provides details about the API endpoint for the chrome-extension backend which performs operations for transcribing videos with timestamps.

## Description

The video file is converted to an audio file, which is then transcribed to text using openAI's [Whisper](https://github.com/openai/whisper).

## Base URL

The base URL for all API endpoints is:

**`https://chrome-exx-937e6f500932.herokuapp.com/`**

## Endpoints

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
    "Transcription": "00:00- you"
  }
]
