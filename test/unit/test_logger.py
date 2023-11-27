from main import get_logger


def test_should_make_a_log_with_provider(mocker):
    class MockedProvider:
        pass

    mocked_function = mocker.Mock()

    MockedProvider.debug = mocked_function

    logger = get_logger(provider=MockedProvider)

    logger.debug('debug')

    mocked_function.assert_called_once_with('debug')


def test_should_make_a_log_with_context(mocker):
    class MockedProvider:
        pass

    mocked_method = mocker.Mock()

    MockedProvider.debug = mocked_method

    logger = get_logger(provider=MockedProvider, context={'key': 'value'})

    logger.debug('debug')

    mocked_method.assert_called_once_with('debug [Context: key=value]')
