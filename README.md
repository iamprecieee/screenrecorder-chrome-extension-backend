# Chrome Extension Backend

This contains the backend code for a screenrecorder chrome extension plugin, which provides a RESTful API for managing video retrieval, saving to disk, and transcription.


## Installation

To run the Chrome Extension Backend locally, follow these steps:

1. **Clone the Repository and Activate the Virtual Environment:** 
   ```bash
   git clone https://github.com/iamprecieee/screenrecorder-chrome-extension-backend.git
   cd chrome
   python3 -m venv venv   # Creates a virtual environment
   source venv/bin/activate  # Activates the virtual environment (Windows users: use venv\Scripts\activate)
   ```

2. **Install Required Dependencies:** 
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Configuration:** 
   - Create a `config.py` file and configure the necessary environment variables, such as upload details, swagger API config, max file content length, and other configuration settings.

4. **Run the App:** 
   ```bash
   flask run # OR `python3 app.py`
   ```

## Structure
* [Init](resources/__init__.py) - This creates and configures the Flask application.
* [Config](resources/config.py) - This handles the configuration variables for the entire app.
* [Utils](resources/utils.py) - This module contains all necessary helper functions for views.py
* [Views](resources/views.py) - This contains the endpoints necessary for operations on recorded video files.
* [App](app.py) - This handles application running with necessary variables set in [flaskenv](.flaskenv).


## Documentation
For detailed documentation on the API endpoints and their usage, please refer to the following:

- [Video Upload](UPLOAD_DOCUMENTATION.md) file.
- [Video Playback](VPLAYBACK_DOCUMENTATION.md) file.
- [Video List Retrieval](RETRIEVAL_DOCUMENTATION.md) file.
- [Video Transcription](TRANSCRIPTION_DOCUMENTATION.md) file.

## Swagger UI and Live Link
- [Swagger](https://chrome-exx-937e6f500932.herokuapp.com/swagger-ui)
- [Live Link](https://chrome-exx-937e6f500932.herokuapp.com/)

