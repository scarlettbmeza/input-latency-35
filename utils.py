import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    """
    Makes a GET request to a specified URL with retry logic.
    Retries the request in case of a network failure.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response if successful
        except RequestException as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts < max_retries:
                time.sleep(delay)  # Wait before retrying
            else:
                print("Max retries reached. Exiting.")
                raise

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f"Failed to fetch data: {e}")
