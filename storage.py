import os
from settings.conf import LOG_DIR, FILES_DIR


def get_file_link(file_name: str, storage: str) -> str:
    file_link = None
    if storage == 'local':
        file_link = os.path.join(FILES_DIR, f'{file_name}.csv')
    # elif storage == 'aws':
    #     file_link = None
    return file_link
