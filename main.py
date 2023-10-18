from flask import Flask, request, jsonify, make_response, Response
import mysql.connector
# from flask_mysqldb import MySQL

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root1",
    password="rootroot12345",
    database="carhire"
)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    cursor = db.cursor()
    try:
        insert_query = "INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (data['first_name'], data['last_name'], data['email'], data['phone_number']))
        db.commit()
        return jsonify({'message': 'Customer added successfully'})
    except Exception as error:
        error_message = {'message': str(error)}
        response = make_response(jsonify(error_message), 400)  # 400 Bad Request status code
        return response


@app.route('/update_customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    cursor = db.cursor()
    update_query = "UPDATE Customers SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE customer_id = %s"
    cursor.execute(update_query, (data['first_name'], data['last_name'], data['email'], data['phone_number'], customer_id))
    db.commit()
    if cursor.rowcount > 0:
        # Fetch the updated customer data
        cursor.execute("SELECT * FROM Customers WHERE customer_id = %s", (customer_id,))
        updated_customer = cursor.fetchone()
        if updated_customer:
            customer_data = {
                'customer_id': updated_customer[0],
                'first_name': updated_customer[1],
                'last_name': updated_customer[2],
                'email': updated_customer[3],
                'phone_number': updated_customer[4]
            }
            return jsonify({'message': 'Customer updated successfully', 'customer': customer_data})
        else:
            return jsonify({'message': 'Failed to fetch updated customer data'})
    else:
        return jsonify({'message': 'no changes made'})


@app.route('/delete_customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Customers WHERE customer_id = %s", (customer_id,))
    existing_customer = cursor.fetchone()
    print(existing_customer)
    if existing_customer:
        # If the customer exists, delete them
        delete_query = "DELETE FROM Customers WHERE customer_id = %s"
        cursor.execute(delete_query, (customer_id,))
        db.commit()
        return jsonify({'message': 'Customer deleted successfully'})
    else:
        # If the customer does not exist, provide an appropriate response
        return jsonify({'message': 'Customer not found'})

@app.route('/get_customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    cursor = db.cursor()
    select_query = "SELECT customer_id, first_name, last_name, email, phone_number FROM Customers WHERE customer_id = %s"
    cursor.execute(select_query, (customer_id,))
    result = cursor.fetchone()
    if result:
        customer_data = {
            'customer_id': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'email': result[3],
            'phone_number': result[4]
        }
        return jsonify(customer_data)
    return jsonify({'message': 'Customer not found'})

if __name__ == '__main':
    app.run(host='0.0.0.0',port=5000,debug=True)
