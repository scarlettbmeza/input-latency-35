import time
import random
import requests
from requests.exceptions import RequestException

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    """
    Retries a network request up to 'retries' times with a 'delay' in seconds.
    Raises NetworkError if all retries fail.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON content on success
        except RequestException:
            if attempt < retries - 1:
                # Exponential backoff strategy
                backoff_time = delay * (2 ** attempt)
                print(f'Retry {attempt + 1}/{retries} failed. Retrying in {backoff_time} seconds...')
                time.sleep(backoff_time)
            else:
                print('All retries failed. Raising NetworkError.')
                raise NetworkError(f'Failed to retrieve data from {url}')