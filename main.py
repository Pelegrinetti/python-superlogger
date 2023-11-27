import logging

from src.abstract import AbstractLoggerProvider


class Logger:
    _logger: AbstractLoggerProvider
    _context: dict

    def __init__(
        self,
        provider: AbstractLoggerProvider | None = None,
        context: dict | None = None,
    ) -> None:
        self._logger = provider if provider is not None else logging.getLogger()
        self._context = context

    def _has_context(self) -> bool:
        return self._context is not None

    def _add_context(self, message: str) -> str:
        if not self._has_context():
            return message

        context_items = ''.join(
            [f'{key}={value}' for key, value in self._context.items()]
        )

        return f'{message} [Context: {context_items}]'

    def debug(self, message: str) -> None:
        to_log = self._add_context(message)

        self._logger.debug(to_log)

    def info(self, message: str) -> None:
        to_log = self._add_context(message)

        self._logger.info(to_log)

    def warning(self, message: str) -> None:
        to_log = self._add_context(message)

        self._logger.warning(to_log)

    def error(self, message: str) -> None:
        to_log = self._add_context(message)

        self._logger.error(to_log)

    def critical(self, message: str) -> None:
        to_log = self._add_context(message)

        self._logger.critical(to_log)


def get_logger(
    provider: AbstractLoggerProvider | None = None, context: dict | None = None
) -> Logger:
    return Logger(provider, context)
