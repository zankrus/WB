import requests


class SomeClient:
    BASE_URL = "https://petstore3.swagger.io"
    CREATE_USER = "/api/v3/user"

    def __init__(self, username, password):
        """Конструктор класса SomeClient"""
        self.s = requests.session()
        self.username = username
        self.password = password
        self.hostname = "https://petstore3.swagger.io"

    def post_create_user(self, data : dict):
        res = self.s.post(
            self.hostname + self.CREATE_USER, json=data
        )
        return res

    def put_edit_user(self,username : str, data : dict):
        res = self.s.put(
            self.hostname + self.CREATE_USER + f"/{username}", json=data
        )
        return res

    def get_user(self, username: str):
        res = self.s.get(
            self.hostname + self.CREATE_USER + f"/{username}"
        )
        return res

    def delete_user(self, username: str):
        res = self.s.delete(
            self.hostname + self.CREATE_USER + f"/{username}"
        )
        return res
