class Config:
    DEBUG = True
    TESTING = True

    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://jrdarwin:D4rw1n2024*@localhost:3306/db_webpersonal"
    )


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
