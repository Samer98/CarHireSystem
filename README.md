# Car Hire Management System 🚀

This is a simple Flask-based application for managing a car rental system. It allows you to perform basic operations such as adding, updating, deleting, and retrieving customer information from a MySQL database.

## Prerequisites 🚀

Before running the application, make sure you have the following installed:

- Python
- Flask
- MySQL
- MySQL Connector
- Decouple

## Installation 🚀

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/car-hire-management.git
   cd car-hire-management
   
    Create a .env file in the project directory and add your database configuration. For example:
    .env
   
   Install the libraries using pip install -r requirements.txt

DB_HOST=localhost
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_NAME=carhire

Install the required Python packages:

bash

pip install Flask mysql-connector-python decouple

Start the Flask application:

bash

    python app.py

The application should now be running on http://localhost:5000.
Usage
# 1. Get Customer Information 🚀

Retrieve customer information by providing a valid customer_id:

    Method: GET
    URL: /get_customer/<int:customer_id>
    Response: Customer details in JSON format

# 2. Add a New Customer 🚀

Add a new customer to the database:

    Method: POST
    URL: /add_customer
    Request Body: Customer data in JSON format (e.g., {"first_name": "John", "last_name": "Doe", "email": "john@example.com", "phone_number": "1234567890"})
    Response: Success message and customer data in JSON format

# 3. Update Customer Information 🚀

Update customer information by providing a valid customer_id and new data:

    Method: PUT
    URL: /update_customer/<int:customer_id>
    Request Body: New customer data in JSON format (e.g., {"first_name": "Updated Name", "last_name": "Updated Last Name", "email": "updated@example.com", "phone_number": "9876543210"})
    Response: Success message and updated customer data in JSON format

# 4. Delete Customer 🚀

Delete a customer by providing a valid customer_id:

    Method: DELETE
    URL: /delete_customer/<int:customer_id>
    Response: Success message

