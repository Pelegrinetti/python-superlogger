from src.logger import Logger
from src.abstract import AbstractLoggerProvider


def get_logger(
    provider: AbstractLoggerProvider | None = None, context: dict | None = None
) -> Logger:
    return Logger(provider, context)
