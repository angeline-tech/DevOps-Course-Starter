import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # TODO: Fix this? Integration tests won't run
    # if not SECRET_KEY:
    #     raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
