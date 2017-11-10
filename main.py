from pathlib import Path

import sys

import os

import yaml


class Node:
    def __init__(self):
        self.folder = ""
        self.include_files = []
        self.include_folders = []
        self.exclude_folders = []


class Constants:
    class Keys:
        storage_path = "storage"

    class Default:
        config_file = ".quantum_cloning.yaml"
        config_file_path = "{0}/{1}".format(str(Path.home()), config_file)


class Config:
    def __init__(self, config_file=Constants.Default.config_file_path):
        assert os.path.isfile(config_file), """Create configuration file `{0}` in your home 
        directory ({1})""".format(Constants.Default.config_file, str(Path.home()))

        file = open(config_file, "r", encoding="utf-8")
        configs = yaml.load(file)
        self.storage_path = configs[Constants.Keys.storage_path]
        assert (self.storage_path is not None), 'Provide storage path "{}""'.format(Constants.Keys.storage_path)

        assert os.path.isdir(self.storage_path), "Storage path '{}' doesn't exist".format(self.storage_path)

        self.backup_file = ""
        self.backup_folder = ""


if len(sys.argv) > 1:
    config = Config(sys.argv[1])
else:
    config = Config()
