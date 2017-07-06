import hashlib
from urllib import parse

class Gravatar:
    __hash = ''
    __url = 'https://gravatar.com/avatar/'
    __params = {}

    def __init__(self, email: str, **kwargs):
        self.email = email
        self.__params = kwargs

    def __str__(self) -> str:
        return Gravatar.__url + self.hash + self.query

    def set(self, **kwargs):
        self.__params = {**self.__params, **kwargs}

    @property
    def hash(self) -> str:
        return self.__hash.hexdigest()

    @property
    def email(self):
        pass

    @email.setter
    def email(self, email: str) -> None:
        self.__hash = hashlib.md5(email.encode('utf-8'))

    @property
    def size(self) -> int:
        if ('s' in self.__params):
            return self.__params.get('s')
        else:
            return 80

    @size.setter
    def size(self, pixels: int) -> None:
        self.__params['s'] = pixels

    @property
    def query(self) -> str:
        if (len(self.__params) > 0):
            return '?' + parse.urlencode(self.__params)
        else:
            return ''
