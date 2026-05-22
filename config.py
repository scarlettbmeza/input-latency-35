import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_config(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as config_file:
                try:
                    file_config = json.load(config_file)
                    self.config.update(file_config)
                except json.JSONDecodeError:
                    print('Error: Invalid JSON format in config file.')

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    defaults = {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 70
    }
    config_loader = ConfigLoader(defaults)
    config_loader.load_config('config.json')
    print(config_loader.config)  # This will print merged configuration
