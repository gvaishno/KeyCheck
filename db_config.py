from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'playersn_keycheck'
app.config['MYSQL_DATABASE_PASSWORD'] = 'K8grACPjxtmEAnY'
app.config['MYSQL_DATABASE_DB'] = 'playersn_keycheck'
app.config['MYSQL_DATABASE_HOST'] = '209.133.198.22'
mysql.init_app(app)
