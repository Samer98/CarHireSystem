from flask import Flask, request, jsonify, make_response, Response
import mysql.connector
# from flask_mysqldb import MySQL
from decouple import config

from database import DataBaseQueries

app = Flask(__name__)

db_host = config('DB_HOST')
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_name = config('DB_NAME')

# Create a database connection
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

db_queries = DataBaseQueries(db)
@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    try:
        db_queries.insert_customer(data)
        return jsonify({'message': 'Customer added successfully',"data":data})
    except Exception as error:
        error_message = {'message': str(error),"data":[]}
        response = make_response(jsonify(error_message), 400)  # 400 Bad Request status code
        return response


@app.route('/update_customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    db_queries.update_customer(data,customer_id)
    if db_queries.cursor.rowcount > 0:
        # Fetch the updated customer data
        customer = db_queries.get_customer(customer_id)
        customer = db_queries.cursor.fetchone()
        if customer:
            updated_customer =db_queries.customer_info(customer)

            return jsonify({'message': 'Customer updated successfully', 'data': updated_customer})
        else:
            return make_response(jsonify({'message': 'Failed to fetch updated customer data',"data":[]}), 400)
    else:
        return make_response(jsonify({'message': 'No changes made',"data":[]}), 204)


@app.route('/delete_customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    db_queries.get_customer(customer_id)
    existing_customer = db_queries.cursor.fetchone()
    if existing_customer:
        # If the customer exists, delete them
        db_queries.delete_customer(customer_id)
        return jsonify({'message': 'Customer deleted successfully','data':[]})
    else:
        # If the customer does not exist, provide an appropriate response
        return make_response(jsonify({'message': 'Customer not found',"data":[]}), 400)

@app.route('/get_customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    db_queries.get_customer(customer_id)
    customer = db_queries.cursor.fetchone()
    if customer:
        customer_data= db_queries.customer_info(customer)
        return jsonify({"data":customer_data})
    return make_response(jsonify({'message': 'Customer not found',"data":[]}), 400)

if __name__ == '__main':
    app.run(host='0.0.0.0',port=5000,debug=True)
