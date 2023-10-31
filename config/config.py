import json
import os


class Config:
    """
    Configuração base
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Configuração para ambiente de desenvolvimento
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Configuração para ambiente de produção
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
