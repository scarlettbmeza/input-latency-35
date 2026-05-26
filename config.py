import json
import os

DEFAULT_CONFIG = {
    'graphics': {
        'resolution': '1920x1080',
        'fullscreen': True,
        'vsync': True,
    },
    'controls': {
        'mouse_sensitivity': 1.0,
        'invert_y_axis': False,
    },
    'audio': {
        'master_volume': 100,
        'music_volume': 80,
        'effects_volume': 80,
    }
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
                self.config = self._merge_configs(DEFAULT_CONFIG, user_config)

    def _merge_configs(self, default, user):
        for key, value in user.items():
            if isinstance(value, dict) and key in default:
                default[key] = self._merge_configs(default[key], value)
            else:
                default[key] = value
        return default

    def get(self, key, default=None):
        return self.config.get(key, default)

