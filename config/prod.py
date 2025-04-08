class ProdConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'  # 本番用に仮設定
    SQLALCHEMY_TRACK_MODIFICATIONS = False