import pprint
import requests
from json import loads


def test_post_v1_account():
    # Регистрация пользователя

    login = 'linara5'
    email = f'{login}@mail.ru'
    password = '123456789'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account', json=json_data)
    assert response.status_code == 201, "Пользователь не был создан"
    # print(response.status_code)
    # print(response.text)

    # Получить письма из почтового сервера

    params = {
        'limit': '10'
    }

    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Письма не были получены"

    # Получить активационный токен
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            print(token)

    assert token is not None, f"Токен для пользователя {login} не был получен"

    # Активация пользователя

    response = requests.put(f'http://5.63.153.31:5051/v1/account/{token}')
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не был активирован"

    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не был авторизован"