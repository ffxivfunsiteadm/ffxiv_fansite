from flask import Flask
from .configs.init import init_config

def create_app(config_name='dev'):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    init_config(app, config_name)
    
    from .core.blueprints import main_bp
    app.register_blueprint(main_bp)
    
    return app