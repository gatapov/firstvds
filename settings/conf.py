import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FILES_DIR = os.path.join(BASE_DIR, 'files')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

STORAGE = 'local'   # aws

