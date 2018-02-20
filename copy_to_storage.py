import os
from distutils.dir_util import copy_tree
from pathlib import Path

import yaml

from config import Config
from source_object import SourceObject


class CopyToStorage:
    def __init__(self):
        config = Config()

        backup_sources = []
        source_path = os.getcwd()
        for file_name in os.listdir(source_path):
            file_name = os.path.join(source_path, file_name)
            file = open(file_name, "r", encoding="utf-8")
            source_config = yaml.load(file)
            source = SourceObject(source_config)
            backup_sources.append(source)

        for backup_source in backup_sources:
            for source in backup_source.sources:
                from_directory = os.path.join(Path.home(), source.folder)
                destination_directory = os.path.join(config.storage_path, source.folder)
                copy_tree(from_directory, destination_directory)


CopyToStorage()
