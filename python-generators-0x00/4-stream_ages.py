import seed

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:  # ✅ Loop 1: yields one age at a time
        yield age

    cursor.close()
    connection.close()

def compute_average_age():
    """Calculates average age using the generator without loading all data."""
    total = 0
    count = 0

    for age in stream_user_ages():  # ✅ Loop 2: aggregates on the fly
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")
