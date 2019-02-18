'''Application configuration file'''
import os

class Config:
    """Parent configuration class"""
    DEBUG = False
    SECRET = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class DevelopmentConfig(Config):
    """Development environment configurations"""
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL")

class TestingConfig(Config):
    """Testing environment configurations"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("TEST_DATABASE_URL")

class StagingConfig(Config):
    """Staging environment configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment configurations"""
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv("DATABASE_URL") # Specify database URL for production deployment

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}