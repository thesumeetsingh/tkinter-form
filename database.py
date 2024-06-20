import mysql.connector

def insert_data(name, branch, gender, contact, email, address):
    try:
        # Establish the connection to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="pythonForm"
        )
        
        cursor = connection.cursor()
        
        # Insert the data into the userdetail table
        insert_query = """
        INSERT INTO userdetail (name, branch, gender, contact, email, address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (name, branch, gender, contact, email, address)
        cursor.execute(insert_query, data)
        
        # Commit the transaction
        connection.commit()
        
        print("Data inserted successfully")
        
    except mysql.connector.Error as error:
        print(f"Failed to insert data into MySQL table {error}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Test the function
# insert_data('John Doe', 'Computer Science', 'Male', '1234567890', 'john@example.com', '123 Street Name')
