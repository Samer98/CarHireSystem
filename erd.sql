use carhire;

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15)
);

CREATE TABLE Vehicles_type (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    capacity VARCHAR(50) NOT NULL
);
INSERT INTO Vehicles_type (type_name, capacity) VALUES
    ('small', "4"),
    ('family', "7"),
    ('vans', "7+");
    
CREATE TABLE Vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT,
    car_name VARCHAR(50),
    availability BOOLEAN,
	FOREIGN KEY (type_id) REFERENCES Vehicles_type(type_id)
);


INSERT INTO Vehicles (type_id, car_name,availability) VALUES
    (1,'bmw', true),
    (2,'suzuki car', false),
    (3,'Truck', true);

CREATE TABLE Bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    vehicle_id INT,
    booking_date DATE,
    confirmation_letter_sent BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id)
);

CREATE TABLE Invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    invoice_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
);



