from python.login import *
import os

"""
Creates user variable of the right kind

If the user shouldn't be allowed to view the page:
    Show the 404 page and exit
    Can handle permissions if all python webpages import this 

Three different kinds of users:
    - Someone not logged in 
    - Normal user
    - Manager
Can add role specific methods like
    Is authorized
    Nav options
    ...
"""


class NotLoggedInUser:

    def __init__(self, email=None):
        self.logged_in = False
        self.email = email

    def is_authorized(self):
        """
        Checks if a user is allowed on a page
        app.py uses SCRIPT_NAME to get name and path to script

        Anyone not logged should only be able to login or signup
        """
        uri = os.environ.get('SCRIPT_NAME') or []
        return uri in ['/webfiles/signup.py', '/index.py']

    def get_nav_items(self):
        return [('Home', 'fas fa-home', '/index.py'),('Update Location', 'fas fa-qrcode', 'webfiles/updateLocation.py')]


class User(NotLoggedInUser):

    def __init__(self, email):
        NotLoggedInUser.__init__(self, email)
        self.logged_in = True

    def get_nav_items(self):
        return super().get_nav_items() + [
            ('User stuff links', 'fas fa-horse', '#!')
        ]

class Manager(User):

    def __init__(self, email):
        User.__init__(self, email)

    def get_nav_items(self):
        return super().get_nav_items() + [
            ('Admin stuff links', 'fas fa-home', '#!')
        ]


def get_user():
    logged_in, email = loggedIn()
    if not logged_in:
        return NotLoggedInUser()
    if isAdmin(email):
        return Manager(email)
    else:
        return User(email)
