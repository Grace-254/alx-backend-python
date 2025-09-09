import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",  # Replace with your actual MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        batch = []
        for row in cursor:  # ✅ Loop 1
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []

        if batch:
            yield batch

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def batch_processing(batch_size):
    """Processes each batch and yields users over age 25."""
    for batch in stream_users_in_batches(batch_size):  # ✅ Loop 2
        for user in batch:  # ✅ Loop 3
            if user['age'] > 25:
                print(user)
