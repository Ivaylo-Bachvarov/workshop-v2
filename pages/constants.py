import os
from dotenv import load_dotenv

load_dotenv('.env')

BASE_URL = 'https://automation-workshop.hacksoft.io'
ROOT_USERNAME = os.getenv('ROOT_USERNAME')
ROOT_PASSWORD = os.getenv('ROOT_PASSWORD')
