import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cdmbi'
    MAIL_SUBJECT_PREFIX = '[LBK]'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
    MAIL_SENDER = ADMIN_EMAIL

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    #TODO: add email info

    MONGO_DBNAME = 'lab-bk-dev'
    # MONGO_HOST = '128.199.148.69'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MONGO_DBNAME = 'lab-bk-test'


class ProductionConfig(Config):
    MONGO_DBNAME = 'lab-bk-data'

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig,
    }
