import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add():
	try:
		json = request.json
		name = json['name']
		description = json['description']	
		if name and description and request.method == 'POST':			
			sqlQuery = "INSERT INTO records(name, description) VALUES(%s, %s)"
			bindData = (name, description)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			response = jsonify('Data added successfully!')
			response.status_code = 200
			return response
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/data')
def browse():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, description from records")
		records = cursor.fetchall()
		response = jsonify(records)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/data/<int:record_id>', methods=['GET'])
def read(record_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, description FROM records WHERE id = %s", record_id)
		empRow = cursor.fetchone()
		response = jsonify(empRow)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/data/<int:record_id>', methods=['PUT'])
def update(record_id):
	try:
		json = request.json
		name = json['name']
		description = json['description']	
		if name and description and record_id and request.method == 'PUT':			
			sqlQuery = "UPDATE records SET name=%s, description=%s WHERE id=%s"
			bindData = (name, description, record_id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			response = jsonify('Data updated successfully!')
			response.status_code = 200
			return response
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/data/<int:record_id>', methods=['DELETE'])
def delete(record_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM records WHERE id =%s", (record_id))
		conn.commit()
		response = jsonify('Data deleted successfully!')
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response
		
if __name__ == "__main__":
    app.run()