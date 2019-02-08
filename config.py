import os

class Config:
    '''
    General configuration parent class
    '''



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
  

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    TESTING = True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'testing': TestConfig
}