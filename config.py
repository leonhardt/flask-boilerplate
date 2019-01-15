class Config(object):
    DEBUG = True

    # Define the database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}'.format('mysql+pymysql', 'root', '1234',
                                                     '192.168.10.22:3306/boilerplate')
    DATABASE_CONNECT_OPTIONS = {}

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

