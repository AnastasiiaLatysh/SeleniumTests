import configparser
import os


class Config(object):
    """
    Class which stores config information
    """
    # create instance of config parser and begin read config file
    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(os.path.abspath(__file__)) + "/configs.conf")

    # read base url and contacts endpoint from configs
    base_url = parser.get('test_parameters', 'base_url')
    path_to_chrome_driver = parser.get('paths', 'path_to_chrome_driver')
