import pytest

from src.abstract import AbstractLoggerProvider


def test_should_implement_abstract_logger_provider():
    AbstractLoggerProvider.__abstractmethods__ = set()

    provider = AbstractLoggerProvider()

    with pytest.raises(NotImplementedError):
        provider.debug('debug')

    with pytest.raises(NotImplementedError):
        provider.info('info')

    with pytest.raises(NotImplementedError):
        provider.warning('warning')

    with pytest.raises(NotImplementedError):
        provider.error('error')

    with pytest.raises(NotImplementedError):
        provider.critical('critical')
