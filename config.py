import logging
import os
from distutils.dir_util import copy_tree
from pathlib import Path

import yaml

from constants import Constants, autolog
from source import Source


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
        storage_path = os.path.join(self.storage_path, self.storage_folder)
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

        backup_sources = []
        for file_name in os.listdir(Constants.Default.source_folder):
            file_name = os.path.join(Constants.Default.source_folder, file_name)
            file = open(file_name, "r", encoding="utf-8")
            source_config = yaml.load(file)
            source = Source(source_config)
            backup_sources.append(source)

        for backup_source in backup_sources:
            for source in backup_source.sources:
                from_directory = os.path.join(Path.home(), source.folder)
                destination_directory = os.path.join(storage_path, source.folder)
                copy_tree(from_directory, destination_directory)
