from app import app
from flaskext.mysql import  MySQL

mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''  # need to provide the database name here -- yld_data/wx_data
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)