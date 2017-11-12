from pathlib import Path


def autolog(message):
    "Automatically log the current function details."
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("%s: %s in %s:%i" % (
        message,
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))


class Constants:
    class Keys:
        class Source:
            name = 'name'
            sources = 'sources'
        source_name = 'name'
        storage_path = 'storage'
        source_folder = 'folder'
        storage_folder = 'folder'
        include_folder = 'includeFolders'

    class Default:
        source_folder = 'source'
        storage_folder = 'QuantumCloning'
        config_file = '.quantum_cloning.yaml'
        config_file_path = "{}/{}".format(str(Path.home()), config_file)
