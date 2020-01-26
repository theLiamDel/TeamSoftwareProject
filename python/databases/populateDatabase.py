from python.databases.connectToDatabase import connect
from python.password import Password
connection, cursor = connect()


def populate_users_table():
    """
    This method populates the users table
    """

    print("Populating users table")
    _hashed_password = Password("123")
    try:
        cursor.execute("""INSERT INTO users (fname, lname, password, role) 
                          VALUES ('Liam', 'de la Cour', ? , 1)""", (str(_hashed_password), ))
        connection.commit()
        print("Populated users table")
    except Exception as e:
        print(e)


def populate_products_table():
    """
    This method populates the products table
    """

    print("Populating products table")

    try:
        sql = "INSERT INTO products (title, description, location, comments) VALUES (?, ?, ?, ?)"

        val = [
            ("Cod", "Some smelly Cod", 1, 1),
            ("Salmon", "Tasty Salmon", 10, 2),
            ("Strawberries", "Eww", 20, 3),
            ("Pineapples", "Pen Pineapple Apple Pen", 22, 4)
        ]

        cursor.executemany(sql, val)
        connection.commit()

        print("Populated products table")


    except Exception as e:
        print(e)


def populate_locations_table():
    """
    This method populates the locations table
    """

    print("Populating locations table")

    try:
        sql = "INSERT INTO locations (title, description, comments, location_type, map) VALUES (?, ?, ?, ?, ?)"

        val = []

        for i in range(1,37):
            val.append(("Generic Storage Shelf %d" % i, "Where stuff is stored", 5, 1, "/TeamSoftwareProject/images/locations/%d.png" % i))

        cursor.executemany(sql, val)
        connection.commit()

        print("Populated locations table")


    except Exception as e:
        print(e)


if __name__ == "__main__":
    populate_users_table()
    populate_products_table()
    populate_locations_table()

