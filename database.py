import os

from deta import Deta  # pip install deta
from dotenv import load_dotenv  # pip install python-dotenv


# Load the environment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

class DetaDB:
    def __init__(self, DETA_KEY):
        self.deta = Deta(DETA_KEY)
        self.db = self.deta.Base("users_db")

    def insert_user(self, username, name, password):
        """Returns the user on a successful user creation, otherwise raises and error"""
        return self.db.put({"key": username, "name": name, "password": password})

    def fetch_all_users(self):
        """Returns a dict of all users"""
        res = self.db.fetch()
        return res.items

    def get_user(self, username):
        """If not found, the function will return None"""
        return self.db.get(username)

    def update_user(self, username, updates):
        """If the item is updated, returns None. Otherwise, an exception is raised"""
        return self.db.update(updates, username)

    def delete_user(self, username):
        """Always returns None, even if the key does not exist"""
        return self.db.delete(username)

deta_db = DetaDB(DETA_KEY)