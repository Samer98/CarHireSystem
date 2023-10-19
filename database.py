class DataBaseQueries:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def insert_customer(self,data):
        cursor = self.cursor
        insert_query = "INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (data['first_name'], data['last_name'], data['email'], data['phone_number']))
        self.connection.commit()

    def update_customer(self,data,customer_id):
        cursor = self.cursor
        update_query = "UPDATE Customers SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE customer_id = %s"
        cursor.execute(update_query,(data['first_name'], data['last_name'], data['email'], data['phone_number'], customer_id))
        self.connection.commit()

    def delete_customer(self,customer_id):
        cursor = self.cursor
        delete_query = "DELETE FROM Customers WHERE customer_id = %s"
        cursor.execute(delete_query, (customer_id,))
        self.connection.commit()

    def get_customer(self,customer_id):
        cursor = self.cursor
        get_query = "SELECT customer_id, first_name, last_name, email, phone_number FROM Customers WHERE customer_id = %s"
        cursor.execute(get_query, (customer_id,))

    def customer_info(self,customer):
        customer_data = {
            'customer_id': customer[0],
            'first_name': customer[1],
            'last_name': customer[2],
            'email': customer[3],
            'phone_number': customer[4]
        }
        return customer_data