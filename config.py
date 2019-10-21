class Config:
    '''
    General configurations (configs) parent class
    '''
    SECRET_KEY='minuteWise123'

class ProdConfig(Config):
    '''
    Production configs child class
    
    Args:
        Config: The parent config class with General configs settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configs child class
    
    Args:
        Config: The parent config class with General configs settings
    '''
    
    DEBUG = True