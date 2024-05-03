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
def test_get_positive(client_non_auth, userName, statusCode, expectedResult):
    """
    Позитивный тест на получение юзера. С параметризацией через @pytest.mark.parametrize и явно через pytest.param
    """
    res = client_non_auth.get_user(userName)
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
def test_get_negative(client_non_auth, userName, statusCode, expectedError):
    """
    Негативный тест на получение юзера. С параметризацией через @pytest.mark.parametrize
    """
    res = client_non_auth.get_user(userName)
    assert res.status_code == statusCode
    assert expectedError in res.json()['message']
    # по желанию проверка хедеров и кук


## Пример явной параметризации фикстуры
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


## Пример НЕявной параметризации фикстуры
@pytest.mark.parametrize("user,password", [("some", "some_pass")])
def test_get_positive_with_implicit_param_fixture(client_with_implicit_auth, user, password):
    """
    Пример параметризации через параметризованную фикстуру clientParametrized с неявной передачей.
    В чем соль - фикстура client_with_implicit_auth ожидает 2 фикстуры на вход user, password . Но они не существуют. Они будут создаваться
    в процессе выполнения
    """
    cl = client_with_implicit_auth
    res = cl.get_user("theUser")
    assert res.status_code == 200
    assert res.json() == {'id': 10, 'username': 'theUser', 'firstName': 'John',
                          'lastName': "James' and 1 = if(5=5, sleep(2), 0) and '1'='1", 'email': 'john@email.com',
                          'password': '12345', 'phone': '12345', 'userStatus': 1}


def test_post_create_user_positive(client_non_auth):
    """
    Позитивный сценарий на создание юзера и проверка совпадения данных через ручку получения юзера
    """

    test_data = {
        "id": 14430,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }
    res = client_non_auth.post_create_user(data=test_data)
    assert res.status_code == 200
    assert res.json() == test_data

    getUserResult = client_non_auth.get_user("theUser")
    assert res.json() == getUserResult.json()


def test_post_create_user_positive_db(client_non_auth):
    """
    Позитивный сценарий на создание юзера и проверка совпадения данных через запрос в БД.
    Лучше такое в юниты вынести, чтобы не тестить клиент к базе, а реальную реализацию
    """

    test_data = {
        "id": 14430,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }
    res = client_non_auth.post_create_user(data=test_data)
    assert res.status_code == 200
    assert res.json() == test_data

    ##DB client делаем запрос в базу


def test_post_create_user_negative(client_non_auth):
    """
   Используем тест-дизайн и генерируем проверки. ( Невалидные данные, уже созданные юзеры, удаленные юзеры ( при софт делете)
   В идеале используем знания, какие юниты у нас уже есть, что неплодить дорогие проверки "маппингов" или
   не делать проверки типов данных, если у нас жесткий контракт.
    """
    assert True


def test_put_edit_user_positive(client_non_auth):
    """
    Позитивный сценарий на изменение юзера и проверка совпадения данных через запрос в ручку получения юзера.
     """
    test_data = {
        "id": 144300,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }
    res = client_non_auth.post_create_user(data=test_data)
    assert res.status_code == 200
    assert res.json() == test_data

    getUserResult = client_non_auth.get_user("theUser")
    assert res.json() == getUserResult.json()


def test_put_edit_user_positive_db(client_non_auth):
    """
   Позитивный сценарий на изменение юзера и проверка совпадения данных через запрос в БД. .
    """
    assert True


def test_delete_positive(client_non_auth):
    """
       Позитивный тест на удаление юзера. Проверка через запрос в ручку получения юзера.
       """
    res = client_non_auth.delete_user("User1")
    assert res.status_code == 200
    assert res.json() == {"success": True}

    getUserResult = client_non_auth.get_user("theUser")
    assert getUserResult.status_code == 200
    assert getUserResult.json() == {"success": True}


def test_delete_positive_db(client_non_auth):
    """
       Позитивный тест на удаление юзера. Проверка через запрос к базе
       """
    res = client_non_auth.delete_user("User1")
    assert res.status_code == 200
    assert res.json() == {"success": True}

    getUserResult = client_non_auth.get_user("theUser")
    assert getUserResult.status_code == 200
    assert getUserResult.json() == {"success": True}
