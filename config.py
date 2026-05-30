import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json'):
        self.default_config_path = default_config_path
        self.config = self.load_config()

    def load_config(self):
        # Load default configuration
        config = self.load_json(self.default_config_path)
        # Override with user configuration if exists
        user_config_path = 'user_config.json'
        if os.path.exists(user_config_path):
            user_config = self.load_json(user_config_path)
            config.update(user_config)
        return config

    def load_json(self, filepath):
        # Load JSON data from a specified file
        with open(filepath, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        # Get a configuration value by key
        return self.config.get(key, default)

# Example usage of the ConfigLoader
if __name__ == '__main__':
    config_loader = ConfigLoader()
    screen_resolution = config_loader.get('screen_resolution', '1920x1080')
    print(f'Screen resolution is set to: {screen_resolution}')