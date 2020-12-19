import os


class Config:
    SECRET_KEY = 'abcd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
   #MAIL_SERVER = 'smtp.googlemail.com'
   #MAIL_PORT = 587
   #MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_EMAIL')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')