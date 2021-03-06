from python.databases.databaseQueries import select_all, select_all_with_conditions, get_product_that_expires_on
from datetime import datetime

table = '''
<div class="card spur-card">
    <div class="card-header">
        <div class="spur-card-icon">
            <i class="fas fa-table"></i>
        </div>
        <div class="spur-card-title">%s</div>
    </div>
    <div class="card-body ">
        <table class="table table-hover table-in-card">
            <thead>
                <tr>
                    <th scope="col">Product</th>
                    <th scope="col">Description</th>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
        </table>
    </div>
</div>
'''


def create_table_of_locations():
    """
    This function will create a html table containing all products and information for each location

    Returns:
        output -- The string containing the html of the tables
    """

    locations = select_all("locations")

    output = "<section>"

    for location in locations:

        output += create_table_of_products_from_location(location['id'], location['title'])

    output += "</section>"

    return output


def create_table_of_products_from_location(location_id, location_name):
    """
    This function creates a table from the products stores in a location

    Arguments:
        location_id - int representing the id of the location
        location_name - String representing the name of the location

    Returns:
        output - String containing the table of products
    """

    output = ""

    products_stored_in_location = select_all_with_conditions("products", "location", location_id)

    for product in products_stored_in_location:
        output += "<tr><td scope='row'>%s</td><td>%s</td></tr>" % (product['title'], product['description'])


    return table % (location_name, output)


def create_table_of_products_that_expire_today():
    """
    Creates a html table containing info about products whose expiry is today
    """

    todays_date = datetime.date(datetime.now())

    products_expiring = get_product_that_expires_on(todays_date)

    output = "<section><table>"

    output += "<tr><th>%s</th><th>%s</th></tr>" % ("Product Name", "Location")

    for product in products_expiring:
        output += "<tr><td>%s</td><td>%s</td></tr>" % (product['title'], product['location'])

    output += "</table></section>"

    return output


if __name__ == "__main__":
    print(create_table_of_locations())
    print(create_table_of_products_that_expire_today())

