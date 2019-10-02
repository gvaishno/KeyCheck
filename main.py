import pymysql
import json
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash
application = app

@app.route('/')
def indexpage():
    return 'A Hackerfoss Project'

@app.route('/range', methods=['GET'])
def range():
	id = request.args.get('id')
	id = '%' + id + '%'
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		cursor.execute("SELECT * FROM keylist WHERE keylist LIKE %s", id)
		row = cursor.fetchone()
		resp = str(row)
		resp = json.dumps(row['keylist'])
		resp = resp[:-3]
		resp = resp.replace('"', '')
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' #+ request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(500)
def server_error(error=None):
    message = {
        'status': '404',
        'message': 'Id Not Found/ or Something Went Wrong!',
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
