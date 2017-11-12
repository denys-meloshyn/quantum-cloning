from constants import Constants


class Node:
    def __init__(self, source, source_name):
        self.folder = source[Constants.Keys.source_folder]
        assert (self.folder is not None), 'Folder must be not empty {}'.format(source_name)

        self.include_files = []
        self.include_folders = []
        for folder in source.get(Constants.Keys.include_folder, []):
            self.include_folders.append(Node(folder, ''))
        self.exclude_folders = []

    def __repr__(self):
        return '{} folder: {}, include_files: {}, include_folders: {}, exclude_folders:{}'.format(self.__class__,
                                                                                                  self.folder,
                                                                                                  self.include_files,
                                                                                                  self.include_folders,
                                                                                                  self.exclude_folders)
