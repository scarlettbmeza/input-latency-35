import time
import random

class NetworkError(Exception):
    pass

def retry(func, retries=3, delay=2):
    """
    Retry a function if it raises a NetworkError.
    Args:
        func: The function to call.
        retries: Number of retry attempts.
        delay: Delay in seconds before retrying.
    """
    for attempt in range(retries):
        try:
            return func()
        except NetworkError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)  # Delay before retrying
    raise NetworkError(f"Function failed after {retries} attempts")

# Example function to demonstrate retry

def unreliable_network_operation():
    """
    Simulate a network operation that may fail.
    Raises:
        NetworkError: Randomly raises an error to simulate failure.
    """
    if random.choice([True, False]):
        raise NetworkError("Network operation failed")
    return "Success"

# Example of using the retry function
if __name__ == '__main__':
    try:
        result = retry(unreliable_network_operation)
        print(result)
    except NetworkError as e:
        print(e)