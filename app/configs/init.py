from dotenv import load_dotenv
import os

def init_config(app, config_name='dev'):
    load_dotenv()  # .envから環境変数を読み込む
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    if config_name == 'dev':
        app.config.from_object('config.dev.DevConfig')
    else:
        app.config.from_object('config.prod.ProdConfig')