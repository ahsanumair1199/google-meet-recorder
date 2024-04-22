from dotenv import load_dotenv
import os

if load_dotenv():
    print('Loading .env variables')

API_TITLE = os.environ['API_TITLE']
API_DESCRIPTION = os.environ['API_DESCRIPTION']
API_VERSION = os.environ['API_VERSION']
GOOGLE_EMAIL = os.environ['GOOGLE_EMAIL']
GOOGLE_PASSWORD = os.environ['GOOGLE_PASSWORD']
GOOGLE_MEET_LINK = os.environ['GOOGLE_MEET_LINK']
WEBDRIVER_LOG_PATH = os.environ['WEBDRIVER_LOG_PATH']
