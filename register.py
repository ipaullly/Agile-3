
data = []


class Register(object):
    def __init__(self, username, password):
        """This method allows the admin to create a user"""
        self.username = username
        self.password = password
        self.db = data
        self.role = "User"

        # Validate common user data.
        for user in self.db:
            if user['name'] == self.name:
                message = "The name already in use in the system."
                return message

        payload = {"id": len(self.db) + 1, "name": self.name,
                     "password": self.password, "role": self.role}
        data.append(payload)
        return "Successful registration"

    def get_user(self, userid):
        for user in data:
            if user['userid'] == userid:
                return user
            return "The user is not in the system"

    def moderator(self, userid):
        """This method uses the PUT method to cancel a request."""
        for user in data:
            if user['id'] == userid:
                user["role"] = "Moderator"
            return "Not a user in this system"
        return "User role updated"

    def admin(self, userid):
        """This method uses the PUT method to cancel a request."""
        for user in data:
            if user['id'] == userid:
                user["role"] = "Admin"
            return "Not a user in this system"
        return "User role updated"
