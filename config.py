from logging import DEBUG
from dotenv import load_dotenv
from pathlib import Path
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Configuration from environment variables"""

    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP = "run.py"

    # Staement for enabling the development environment
    DEBUG = True

    # Specifying host and port for our server
    HOST = '127.0.0.1'
    PORT = 500

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=san francisco&appid=4647aaef88d6e0fbf8feeb4ce0f0cb50"


