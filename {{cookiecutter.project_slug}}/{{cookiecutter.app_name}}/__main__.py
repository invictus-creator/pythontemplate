"""Main application entry point.

    python -m {{cookiecutter.app_name}} ...

"""
from .cli import get_cli_args
from .core.config import config
from .core.logger import logger


def main():
    """Execute the application."""
    logger.info("Launching program.")
    raise NotImplementedError


# Setup config and logger using cli args
cli_args = get_cli_args()
logger.start(cli_args.loglevel)
config.load(cli_args.config_path)

if __name__ == "__main__":
    raise SystemExit(main())
