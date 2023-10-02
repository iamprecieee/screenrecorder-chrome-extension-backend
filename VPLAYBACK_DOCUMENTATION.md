# API Documentation - Video Playback

This documentation provides details about the API endpoint for the chrome-extension backend which performs operations for serving videos for playback.

## Base URL

The base URL for all API endpoints is:

**`https://chrome-exx-937e6f500932.herokuapp.com/`**

## Endpoints

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


