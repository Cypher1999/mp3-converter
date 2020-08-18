import os 

class config():

    DEBUG=False
    TESTING=False

class development(config):

    DEBUG=True
    TESTING=True
    SECRET_KEY='MysecretKey'
    SERVER_NAME=("127.0.0.1:5000")

class production(config):

    DEBUG=False
    TESTING=False
    SECRET_KEY=os.urandom(24)

