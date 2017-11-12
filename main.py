import logging
import sys

from config import Config

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) > 1:
    config = Config(sys.argv[1])
else:
    config = Config()
