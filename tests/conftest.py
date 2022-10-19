import pytest


@pytest.fixture()
def set_up():
    print('\nВход в систему выполнен')
    yield
    print('Выход из системы выполнен')

# @pytest.fixture(scope='module')
@pytest.fixture(scope='function')
def some():
    print('\nНачало')
    yield
    print('\nКонец')