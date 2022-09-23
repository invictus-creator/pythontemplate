"""Main application entry point.

    python -m {{cookiecutter.app_name}} ...

"""
from .cli import get_cli_args
from .core.config import config
from .core.logger import logger

# Setup config and logger using cli args
cli_args = get_cli_args()
config.load(cli_args.config_path)
logger.start(cli_args.loglevel)


def main():
    """Execute the application."""
    logger.info("Launching program.")
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
