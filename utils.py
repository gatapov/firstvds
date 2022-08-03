import os
from storage import get_file_link


async def check_file_exist(file_name: str, storage: str) -> bool:
    file_link = get_file_link(file_name, storage)
    file_exist = os.path.exists(file_link)
    return file_exist
