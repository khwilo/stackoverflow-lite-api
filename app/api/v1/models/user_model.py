'''This module represents the user entity'''
from passlib.hash import pbkdf2_sha256 as sha256

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
    def generate_password_hash(password):
        '''Generate the hash of the password'''
        return sha256.hash(password)

    @staticmethod
    def verify_password_hash(password, hashed_password):
        '''Compared the password with its hashed value'''
        return sha256.verify(password, hashed_password)

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
