import os

import dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv.load_dotenv(
    os.path.join(os.path.normpath(os.getcwd()), '.env')
)

MAX_RETRIES = os.getenv('MAX_RETRIES', 5)

INSTANCES = os.getenv('INSTANCES', 1)

STATUS_PROCESSING = os.getenv('STATUS_PROCESSING', 36)

STATUS_APPROVED = os.getenv('STATUS_APPROVED', 34)

STATUS_DENY = os.getenv('STATUS_DENY', 35)

WORKERS = int(os.getenv('WORKERS', 1))

DEBUG = True if os.getenv('DEBUG') == 'True' else False

DOMAIN_PATH = os.getenv('DOMAIN_PATH', '')

CSV_NAME = os.getenv('CSV_NAME', '')

EXTENSION = os.getenv('EXTENSION', '')
