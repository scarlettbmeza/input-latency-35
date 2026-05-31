import time
from typing import Any, Dict, List

class LatencyProcessor:
    def __init__(self) -> None:
        self.latencies: List[float] = []

    def add_latency(self, latency: float) -> None:
        if not isinstance(latency, (int, float)):
            raise ValueError('Latency must be a number.')
        if latency < 0:
            raise ValueError('Latency cannot be negative.')
        self.latencies.append(latency)
        print(f'Added latency: {latency}')

    def get_average_latency(self) -> float:
        if not self.latencies:
            raise ValueError('No latencies recorded. Cannot compute average.')
        average = sum(self.latencies) / len(self.latencies)
        print(f'Average latency: {average}')
        return average

    def reset_latencies(self) -> None:
        self.latencies.clear()
        print('Latencies have been reset.')

if __name__ == '__main__':
    processor = LatencyProcessor()
    try:
        processor.add_latency(35.5)
        processor.add_latency(44.0)
        print(processor.get_average_latency())
        processor.reset_latencies()
    except ValueError as e:
        print(f'Error: {e}')