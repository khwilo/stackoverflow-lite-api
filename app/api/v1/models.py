'''This module represents the user entity'''
USERS = [] # Data store for the users

class UserModel:
    '''Entity representation for a user'''
    def __init__(self, username, email, password):
        self.user_id = len(USERS) + 1 # This field represents the primary key
        self.username = username
        self.email = email
        self.password = password

    def get_user_id(self):
        '''Fetch the user id'''
        return self.user_id

    @staticmethod
    def add_user(user):
        '''Add a new user to the data store'''
        USERS.append(user)

    @staticmethod
    def get_user_by_id(user_id):
        '''Fetch a user given a user id'''
        user = {}
        for index, _ in enumerate(USERS):
            if USERS[index].get('user_id') == user_id:
                user = USERS[index]
        return user

    @staticmethod
    def get_user_by_username(username):
        '''Fetch a user given a username'''
        user = {}
        for index, _ in enumerate(USERS):
            if USERS[index].get('username') == username:
                user = USERS[index]
        return user

    @staticmethod
    def get_all_users():
        '''Fetch all users'''
        return USERS

    @staticmethod
    def delete_a_user_by_id(user_id):
        '''Delete a given user given a user id'''
        global USERS
        USERS = list(filter(lambda user: user['user_id'] != user_id, USERS))

    def user_as_dict(self):
        '''Convert the user object into a dictionary'''
        return {
            'user_id' : self.user_id,
            'username': self.username,
            'email'   : self.email,
            'password': self.password
        }
