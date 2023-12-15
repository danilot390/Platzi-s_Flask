from flask_login import UserMixin
from .firestore_service import current_user

class UserData:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password
        
class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        param user_data: UserData
        """  
        self.id = user_data.id
        self.username = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(id):
        user_doc = current_user(id)
        user_data = UserData(
            id = user_doc['id'],
            username = user_doc['username'],
            password = user_doc['password']
        )

        return UserModel(user_data)