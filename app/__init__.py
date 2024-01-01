import os
from flask import Flask
from dotenv import load_dotenv

from app.api.ping import ping_bp
from app.api.v1.analytics import analytics_bp
from config.config import DevelopmentConfig, ProductionConfig

def create_app():
    load_dotenv()

    app = Flask(__name__)
    env = os.getenv('FLASK_ENV')
    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    app.config.from_object(config_map[env])

    app.register_blueprint(ping_bp)
    app.register_blueprint(analytics_bp, url_prefix='/api/v1/analytics')

    return app