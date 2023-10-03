# API Documentation - Video Upload

This documentation provides details about the API endpoint for the chrome-extension backend which performs operations for uploading video chunks.

## Base URL

The base URL for all API endpoints is:

**`https://chrome-exx-937e6f500932.herokuapp.com/`**

## Endpoints

### 2. Upload Video (Chunks)

#### Uploads and appends video chunks to an existing video file on database.

- **Endpoint URL**: `/videos/upload`
- **HTTP Method**: POST

**Description**: Retrieves a blob file containing the recorded video and writes the video to a new file/ appends the video in chunks to a database.

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





