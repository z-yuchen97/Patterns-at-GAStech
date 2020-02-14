USERNAME = 'root'
PASSWORD = 'Root2021@'
HOSTNAME = '127.0.0.1'
DATABASE = 'patterns'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(USERNAME, PASSWORD,
                                                           HOSTNAME, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True