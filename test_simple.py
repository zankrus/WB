import pytest


@pytest.mark.parametrize(
    "userName,statusCode,expectedResult",
    [
        pytest.param(
            "theUser", 200, {'id': 10, 'username': 'theUser', 'firstName': 'John',
                             'lastName': "James' and 1 = if(5=5, sleep(2), 0) and '1'='1", 'email': 'john@email.com',
                             'password': '12345', 'phone': '12345', 'userStatus': 1},
            id="positive")

    ],
)
def test_get_positive(client, userName, statusCode, expectedResult):
    """
    Позитивный тест на получение юзера. С параметризацией через @pytest.mark.parametrize
    """
    res = client.get_user(userName)
    assert res.status_code == statusCode
    assert res.json() == expectedResult
    # по желанию проверка хедеров и кук


@pytest.mark.parametrize(
    "userName,statusCode,expectedError",
    [
        pytest.param(
            "theUser2", 404, "There was an error processing your request. It has been logged",
            id="positive"),
        pytest.param(
            "", 500, "There was an error processing your request. It has been logged",
            id="positive"),
        ## Кол-во кейсов зависит от типа сервиса. Если он внешний, то нужно проверить варианты валидации разных типов данных.
        ## Если внутрянка - то скорее всего нужно проверить соответствие контракту. Без валидаций разных типов данных  ( По примеру Golang Brief )

    ],
)
def test_get_negative(client, userName, statusCode, expectedError):
    """
    Негативный тест на получение юзера. С параметризацией через @pytest.mark.parametrize
    """
    res = client.get_user(userName)
    assert res.status_code == statusCode
    assert expectedError in res.json()['message']
    # по желанию проверка хедеров и кук


def test_get_positive_with_param_fixture(clientParametrized):
    """
    Пример параметризации через параметризованную фикстуру clientParametrized
    Она обернута и тут можно, например, создать авторизованного клиента или нет.
    """
    cl = clientParametrized("theUser", "221052")
    res = cl.get_user("theUser")
    assert res.status_code == 200
    assert res.json() == {'id': 10, 'username': 'theUser', 'firstName': 'John',
                             'lastName': "James' and 1 = if(5=5, sleep(2), 0) and '1'='1", 'email': 'john@email.com',
                             'password': '12345', 'phone': '12345', 'userStatus': 1}
    # по желанию проверка хедеров и кук


@pytest.mark.parametrize(
    "user,password", ["theUser", "221052"])
def test_get_positive_with_implicit_param_fixture(clientParametrized,user,password):
    """
    Пример параметризации через параметризованную фикстуру clientParametrized с неявной передачей.
    В чем соль - фикстура clientParametrized ожидает 2 фикстуры на вход user, password . Но они не существуют. Они будут создаваться
    в процессе выполнения
    """
    cl = clientParametrized("theUser", "221052")
    res = cl.get_user("theUser")
    assert res.status_code == 200
    assert res.json() == {'id': 10, 'username': 'theUser', 'firstName': 'John',
                             'lastName': "James' and 1 = if(5=5, sleep(2), 0) and '1'='1", 'email': 'john@email.com',
                             'password': '12345', 'phone': '12345', 'userStatus': 1}
    # по желанию проверка хедеров и кук



def test_post():
    assert False


def test_put():
    assert False


def test_delete():
    assert False
