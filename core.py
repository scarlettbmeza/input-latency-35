import time
import numpy as np

class GameLogic:
    def __init__(self):
        self.frame_times = []

    def frame_update(self):
        start_time = time.time()
        # Perform game logic updates here
        self.simulate_game_logic()
        elapsed_time = time.time() - start_time
        self.record_frame_time(elapsed_time)

    def simulate_game_logic(self):
        # Simulated game logic computation (e.g., physics, AI)
        np.random.rand(1000)  # Simulate computation workload

    def record_frame_time(self, elapsed_time):
        if len(self.frame_times) >= 100:
            self.frame_times.pop(0)  # Keep the last 100 frame times
        self.frame_times.append(elapsed_time)

    def average_frame_time(self):
        return np.mean(self.frame_times) if self.frame_times else 0.0

    def optimize_logic(self):
        # Implement optimizations for game logic here
        pass

# Example usage
if __name__ == '__main__':
    game = GameLogic()
    for _ in range(150):  # Simulate 150 frames
        game.frame_update()
    print(f'Average Frame Time: {game.average_frame_time()} seconds')