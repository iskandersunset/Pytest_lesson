import pytest


@pytest.fixture()
def test_set_up():
    print('Вход в систему выполнен')


def test_sending_mail_1():
    print('Письмо отправлено')


def test_sending_mail_2():
    print('Письмо отправлено')
