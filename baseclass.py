class DataBaseQueries():


    def insert_customer(self,table_name,data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s' for _ in data.values()])
        values = list(data.values())
        insert_query = "INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
