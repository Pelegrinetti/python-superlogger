# SuperLogger

SuperLogger is a simple and powerful Python logger that provides flexibility and ease of use.

## Summary

1. [Installation](#install)
2. [Usage](#usage)
    - [The Logger class](#the-logger-class)
    - [Basic Usage](#basic-usage)
    - [Creating a Custom Provider](#create-a-custom-provider)
    - [Setting Context for Logging](#set-context-for-logging)
3. [TODO](#todo)

## Installation

You can install SuperLogger using pip or Poetry:

1. Installing with pip:

    ```sh
    pip install superlogger
    ```

2. Installing with Poetry:

    ```sh
    poetry add superlogger
    ```

## Usage

### The Logger class

The `Logger` class is an abstraction around the logging provider. By default, the provider is the `Logger` class from Python's built-in `logging` module. However, SuperLogger allows you to customize the provider.

| Name        | Default             | Required |
| ----------- | ------------------- | -------- |
| `provider`  | `logging.getLogger` | False    |
| `context`   | `None`              | False    |

### Basic Usage

1. Creating an instance of `Logger`:

    ```python
    from superlogger import Logger

    logger = Logger()

    logger.info('[*] Ready to start!! :rocket:')
    ```

2. Creating an instance of `Logger` using the `get_logger` function:

    ```python
    from superlogger import get_logger

    logger = get_logger()

    logger.info('[*] Ready to start!! :rocket:')
    ```

### Creating a Custom Provider

You can use any provider for logging by wrapping it with `AbstractLoggerProvider`. Example:

```python
from superlogger import Logger
from superlogger.abstract import AbstractLoggerProvider

class LoggerProvider(AbstractLoggerProvider):
    # Implement abstract methods here...

# Create an instance of the provider
logger_provider = LoggerProvider()

# Create an instance of the logger with the custom provider
logger = Logger(provider=logger_provider)
```

### Setting Context for Logging

With SuperLogger, you can set context variables for logs, and all subsequent logs will include this context. Example:

```python
from uuid import uuid4 as uuid

from superlogger import Logger

logger = Logger(context={ 'uuid': str(uuid()) })

logger.info("[*] Ready to start!")

# Log: "[*] Ready to start! [Context: uuid="..."]"
```

## TODO

We have a lot of things to do and improve in this library. All constructive ideas are welcome, and I'll be happy to receive them.

- [ ] Settings object
- [ ] Log format setting

More updates coming soon...
