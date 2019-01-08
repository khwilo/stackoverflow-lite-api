'''Run the application'''
import os

from app import create_app

CONFIG_NAME = os.getenv('APP_SETTINGS') # Specify the app settings in production

APP = create_app(CONFIG_NAME) # Application name

if __name__ == '__main__':
    APP.run()
