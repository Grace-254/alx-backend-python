import mysql.connector

def stream_users():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",  # Replace with your actual MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:  # ✅ Only one loop, as required
            yield row

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
