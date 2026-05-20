from typing import List

def average_response_time(times: List[float]) -> float:
    """
    Calculate the average response time from a list of times.

    Args:
        times (List[float]): A list of response times in seconds.

    Returns:
        float: The average response time.
    """
    if not times:
        return 0.0
    return sum(times) / len(times)


def filter_high_latency(responses: List[float], threshold: float) -> List[float]:
    """
    Filter responses that exceed a certain latency threshold.

    Args:
        responses (List[float]): A list of response times in seconds.
        threshold (float): The latency threshold in seconds.

    Returns:
        List[float]: A list of response times exceeding the threshold.
    """
    return [r for r in responses if r > threshold]


def latency_statistics(times: List[float]) -> dict:
    """
    Generate statistics on latencies, including average and maximum values.

    Args:
        times (List[float]): A list of response times in seconds.

    Returns:
        dict: A dictionary with the average and maximum latency.
    """
    average = average_response_time(times)
    maximum = max(times) if times else 0
    return {'average': average, 'maximum': maximum}
