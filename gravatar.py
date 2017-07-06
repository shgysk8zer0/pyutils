import hashlib
class Gravatar:
    __hash = ''
    __url = 'https://gravatar.com/avatar/'
    __params = {}

    def __init__(self, email: str, **kwargs):
        self.__hash = hashlib.md5()
        self.__hash.update(email.encode('utf-8'))
        self.__params = kwargs

    def __str__(self) -> str:
        return Gravatar.__url + self.__hash.hexdigest()
