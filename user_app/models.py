"""The Improved User Model

Mixin classes used to create this class may be found in mixins.py

The UserManager is found in managers.py

"""
from improved_user.model_mixins import AbstractUser


# pylint: disable=too-many-ancestors
class User(AbstractUser):
            """A User model that extends the Improved User"""

def _str_(self):
    return self.email

