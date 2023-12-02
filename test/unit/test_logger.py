from src.main import get_logger


def test_instance_a_default_logger_without_provider():
    logger = get_logger()

    assert logger._logger is not None

def test_should_make_a_log_with_provider(mocker):
    class MockedProvider:
        pass

    mocked_method = mocker.Mock()

    MockedProvider.debug = mocked_method

    logger = get_logger(provider=MockedProvider())

    logger.debug('debug')

    mocked_method.assert_called_once_with('debug')


def test_should_make_a_log_with_context(mocker):
    class MockedProvider:
        pass

    mocked_method = mocker.Mock()

    MockedProvider.debug = mocked_method

    logger = get_logger(provider=MockedProvider(), context={'key': 'value'})

    logger.debug('debug')

    mocked_method.assert_called_once_with('debug [Context: key=value]')

def test_should_make_a_log_without_context(mocker):
    class MockedProvider:
        pass

    mocked_method = mocker.Mock()

    MockedProvider.debug = mocked_method

    logger = get_logger(provider=MockedProvider())

    logger.debug('debug')

    mocked_method.assert_called_once_with('debug')

def test_should_log_all_levels(mocker):
    class MockedProvider:
        pass

    mocked_method = mocker.Mock()

    MockedProvider.debug = mocked_method
    MockedProvider.info = mocked_method
    MockedProvider.warning = mocked_method
    MockedProvider.error = mocked_method
    MockedProvider.critical = mocked_method

    logger = get_logger(provider=MockedProvider())

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

    mocked_method.assert_has_calls([
        mocker.call('debug'),
        mocker.call('info'),
        mocker.call('warning'),
        mocker.call('error'),
        mocker.call('critical'),
    ])
