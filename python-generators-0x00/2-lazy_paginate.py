import seed

def paginate_users(page_size, offset):
    """Fetches a single page of users from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator that lazily yields pages of users one at a time."""
    offset = 0
    while True:  # ✅ Only one loop used
        page = paginate_users(page_size, offset)
        if not page:
            return  # ✅ End of data
        yield page
        offset += page_size
