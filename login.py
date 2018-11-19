
from register import data


class Login(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

        for user in data:
            if user["username"] != self.username\
                and user["password"] != self.password:
                message = "User not available in the system"
                return message

        return "User logged in"




