# Car Hire Management System 🚀

The SQL statements you provided are used to create tables for a car rental management system (ERD).

    Customers:
        customer_id (Primary Key): A unique identifier for each customer.
        first_name: The first name of the customer.
        last_name: The last name of the customer.
        email (Unique): The email address of the customer, which is set as unique to ensure each email is associated with only one customer.
        phone_number: The phone number of the customer.

    Vehicles_type:
        type_id (Primary Key): A unique identifier for each vehicle type.
        type_name: The name of the vehicle type (e.g., "small," "family," "vans").
        capacity: The capacity or maximum number of passengers for this type of vehicle.

    Vehicles:
        vehicle_id (Primary Key): A unique identifier for each vehicle.
        type_id (Foreign Key): References the type_id in the Vehicles_type table, specifying the type of the vehicle.
        car_name: The name or description of the vehicle.
        availability: A boolean indicating whether the vehicle is available (true) or not (false).

    Bookings:
        booking_id (Primary Key): A unique identifier for each booking.
        customer_id (Foreign Key): References the customer_id in the Customers table, indicating the customer associated with the booking.
        vehicle_id (Foreign Key): References the vehicle_id in the Vehicles table, specifying the vehicle booked.
        booking_date: The date of the booking.
        confirmation_letter_sent: A boolean indicating whether a confirmation letter has been sent for this booking (true/false).

    Invoices:
        invoice_id (Primary Key): A unique identifier for each invoice.
        booking_id (Foreign Key): References the booking_id in the Bookings table, indicating the booking associated with this invoice.
        invoice_date: The date the invoice was generated.
        total_amount: The total amount due for this invoice.


Entity-Relationship Diagram (ERD) Explanation:
The ERD represents the relationships between the different tables in your database. Here's a high-level explanation of these relationships:

    Customers can make multiple bookings (one-to-many relationship).
    Vehicles are associated with a specific vehicle type.
    Bookings link customers to specific vehicles.
    Invoices are associated with bookings, indicating the financial transaction for each booking.


This database design allows you to manage customers, vehicles, bookings, and financial transactions efficiently for a car rental system. The relationships between tables are defined by foreign keys, ensuring data integrity and consistency in the database.

![Car Image](erd diiagram.PNG)

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



