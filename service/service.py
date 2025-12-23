from repository import query_database

def fetch_all_bookings():
    """
    Fetches all booking from the database table 'BOOKING'
    """
    client = query_database.DB_Client()
    bookings = client.fetch_bookings("SELECT * FROM BOOKING")
    return bookings
