DEBUG = True
SECRET_KEY = 'secret'

# flask-assets
ASSETS_DEST = 'starter/static/'

# flask-security
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '$2a$10$WyxRXkzAICMHgmqhMGTlJu'

# flask-sqlalchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sql'
