""" Implementation of the command line interface.

"""
import argparse
from pathlib import Path

__all__ = "get_cli_args"


def get_cli_args():
    return _get_argparser().parse_args()


def _get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l', '--log-level',
        dest='loglevel',
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
        default='WARNING'
    )
    parser.add_argument(
        '-c', '--config',
        dest='config_path',
        default=Path('./config.yml'),
        type=_path
    )
    return parser


def _path(path):
    return Path(path)
