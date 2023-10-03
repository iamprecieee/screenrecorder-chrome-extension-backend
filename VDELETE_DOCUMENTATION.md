# API Documentation - Video Playback

This documentation provides details about the API endpoint for the chrome-extension backend which performs deletion of video objects from database.

## Base URL

The base URL for all API endpoints is:

**`https://chrome-exx-937e6f500932.herokuapp.com/`**

## Endpoints

### 3. Delete Video file

#### Retrieves and deletes the requested video file from the database.

- **Endpoint URL**: `/videos/<filename>`
- **HTTP Method**: DELETE
- **Path Parameter**: filename (string): The name of the video file to retrieve.

**Description**: Deletes video file and its content from database.

**Response**:

- Status Code: 204 (No Content)
