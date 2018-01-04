'''
    * Global configurations for app
'''

from src.app_config import Config, ProductionConfig, DevelopmentConfig, TestingConfig

WEBCONFIG = {
    'app_config': DevelopmentConfig,
    'host': 'localhost',
    'port': 3000,
    'static_url_path': '/static',
    'static_folder': 'public',
    'template_folder': 'views',
}