import os
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv()
adventcookie = os.getenv('adventcookie')


def retrieve_input(day,year):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    file_path = f"input_{day}_{year}.txt"
    if not os.path.exists(file_path):
        response = requests.get(url,
                                headers={'cookie': f'session={adventcookie}', 'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            logger.info(f"File downloaded and saved as {file_path}")
        else:
            logger.error(f"Failed to download the file. Status code: {response.status_code}")
    else:
        logger.info(f"The file [{file_path}] already exists.")

def load_input(day,year):
    return open(f"input_{day}_{year}.txt", 'r').read()