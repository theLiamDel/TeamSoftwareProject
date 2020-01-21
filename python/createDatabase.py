from connectToDatabase import connect
connection, cursor = connect()
"""
To generate the tables run the following in the terminal.
python3 createDatabase.py 

Note: You must be in the root of the project directory
"""
def _create_user_db():
    print("creating users table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname VARCHAR(255),
            lname VARCHAR(255),
            password VARCHAR(255),
            role INTEGER,
            image VARCHAR(255)
        );
    """)
    print("created users table")


def _create_product_db():
    print("creating product table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255),
            description TEXT,
            location INTEGER,
            comments INTEGER,
            photo VARCHAR(255)
        );
    """)
    print("created product table")


def _create_location_db():
    print("creating location table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS location(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255),
            description TEXT,
            comments INTEGER,
            map VARCHAR(255)
        );
    """)
    print("created location table")

def createDatabase():
    """
    Function to create the table.
    :return: None
    """
    _create_user_db()
    _create_product_db()
    _create_location_db()

if __name__ == "__main__":
    createDatabase()