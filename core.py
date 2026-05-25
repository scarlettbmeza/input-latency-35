import time
import numpy as np

class GameEngine:
    def __init__(self):
        self.frames = []
        self.last_time = time.time()
        self.frame_rate = 60
        self.delta_time = 0

    def update(self):
        current_time = time.time()
        self.delta_time = current_time - self.last_time
        self.last_time = current_time
        self.frames.append(self.delta_time)
        if len(self.frames) > 100:
            self.frames.pop(0)  # Keep only the last 100 frames

    def get_average_frame_time(self):
        return np.mean(self.frames) if self.frames else 0

    def run(self):
        while True:
            self.update()
            frame_time = self.get_average_frame_time()
            # Here you would render your game frame
            time.sleep(max(0, (1 / self.frame_rate) - frame_time))  # Control frame rate 

if __name__ == '__main__':
    engine = GameEngine()
    engine.run()