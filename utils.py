import time

class LatencyOptimizer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        """Start the latency timer."""
        self.start_time = time.perf_counter()

    def end_timer(self):
        """End the latency timer and return elapsed time in milliseconds."""
        self.end_time = time.perf_counter()
        elapsed_time = (self.end_time - self.start_time) * 1000
        return elapsed_time

    def optimize_function_call(self, func, *args, **kwargs):
        """Wrap function call and measure latency."""
        self.start_timer()
        result = func(*args, **kwargs)
        latency = self.end_timer()
        print(f"Function '{func.__name__}' executed in {latency:.4f} ms")
        return result

# Example usage:
# optimizer = LatencyOptimizer()
# result = optimizer.optimize_function_call(some_function, arg1, arg2)