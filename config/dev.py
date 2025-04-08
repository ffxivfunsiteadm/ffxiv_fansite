class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # 開発用にSQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False