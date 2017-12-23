import os
from pathlib import Path

import yaml

from constants import Constants


class Config:
    def __init__(self, config_file=Constants.Default.config_file_path):
        assert os.path.exists(config_file), """Create configuration file `{}` in your home 
        directory ({})""".format(Constants.Default.config_file, str(Path.home()))

        file = open(config_file, "r", encoding="utf-8")
        configs = yaml.load(file)
        self.storage_path = configs[Constants.Keys.storage_path]
        assert (self.storage_path is not None), 'Provide storage path "{}""'.format(Constants.Keys.storage_path)
        assert os.path.exists(self.storage_path), "Storage path '{}' doesn't exist".format(self.storage_path)

        self.storage_folder = configs.get(Constants.Keys.storage_folder, Constants.Default.storage_folder)
        self.storage_path = os.path.join(self.storage_path, self.storage_folder)
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
