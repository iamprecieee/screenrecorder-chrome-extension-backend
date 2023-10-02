# API Documentation - Video List Retrieval

This documentation provides details about the API endpoint for the chrome-extension backend which performs operations for retrieving video metadata.

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
