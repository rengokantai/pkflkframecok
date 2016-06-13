__author__ = 'Hernan Y.Ke'
class BaseConfig(object):
    SECRET_KEY = ''
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = ''

class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = open('/path/file').read()

class StagingConfig(BaseConfig):
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = ''