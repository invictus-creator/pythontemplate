""" Global application configuration.

This module defines a global configuration object. Other modules should use
this object to store application-wide configuration values.

"""
from yaml import safe_load

from .logger import logger

__all__ = "config", "YamlConfig"


class YamlConfig(dict):
    """ Store YAML configuration data.

    After loading, data can be accessed as dict values.
    """

    def __init__(self, path=None):
        """ Initialize this object.

        :param path: config file path to load
        """
        super(YamlConfig, self).__init__()
        if path:
            self.load(path)
        return

    def load(self, path):
        """ Load data from YAML configuration files.

        :param path: config file path to laod
        """
        with open(path, "r") as stream:
            logger.info(f"Reading config data from '{path}'.")
            data = safe_load(stream)

        try:
            self.update(data)
        except TypeError:  # data is None
            logger.warning(f"Config file '{path}' is empty.")


config = YamlConfig()
