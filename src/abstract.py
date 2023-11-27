from abc import ABC, abstractmethod


class AbstractLoggerProvider(ABC):
    @abstractmethod
    def debug(self, message):
        raise NotImplementedError('Must be implemented')

    @abstractmethod
    def info(self, message):
        raise NotImplementedError('Must be implemented')

    @abstractmethod
    def warning(self, message):
        raise NotImplementedError('Must be implemented')

    @abstractmethod
    def error(self, message):
        raise NotImplementedError('Must be implemented')

    @abstractmethod
    def critical(self, message):
        raise NotImplementedError('Must be implemented')
