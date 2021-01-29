from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'snapbox_db'
app.config['MYSQL_DATABASE_HOST'] = '0.0.0.0'
mysql.init_app(app)