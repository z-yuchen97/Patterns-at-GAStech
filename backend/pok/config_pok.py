USERNAME = 'root'
PASSWORD = 'Root2021@'
HOSTNAME = '127.0.0.1'
DATABASE = 'pok'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD,
                                                           HOSTNAME, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True