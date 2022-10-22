import os

from deta import Deta  # pip install deta
from dotenv import load_dotenv  # pip install python-dotenv
import streamlit_authenticator as stauth

# Load the environment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
#db = deta.Base("users_db_feature_flags")

class users_database:
    def __init__(self, username=None, firstName=None, lastName=None, password=None, email=None, featureFlagId=None, isAdmin=0, database = deta.Base("users_db_main") ):
        # HERE ADD, MANIPILATE, DELETE MODULS
        self.db = database
        # 
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        #self.password = password
        self.password = self.hash_password(password)
        self.email = email
        self.featureFlagId = self.featureFlagId(featureFlagId)
        self.isAdmin =  isAdmin
        # CREATED PARAMETERS
        #self.featureFlagNames=['modul1', 'modul2', 'modul3', 'modul4', 'modul5']
        #self.defaultFeatureFlagId= self.featureFlagId(featureFlagId)
        
    def featureFlagId(self, featureFlagId):
        if featureFlagId == None:
            featureFlagId = [0,1,2]
        else:
            featureFlagId=featureFlagId
        return featureFlagId

    def hash_password(self, password):
        hashed_pass = stauth.Hasher([password]).generate()
        return hashed_pass

    def insert_user(self):
        #User Creation
        self.db.put({"key": self.username \
                    , "firstName": self.firstName \
                    , "lastName": self.lastName \
                    , "password": self.password \
                    , "email": self.email \
                    , "featureFlagId": self.featureFlagId \
                    , "isAdmin": self.isAdmin})
        result = 1
        print('a new user has been added')
        return result

    def fetch_all_users(self):
        """Returns a dict of all users"""
        res = self.db.fetch()
        return res.items

    def get_user(self):
        """If not found, the function will return None"""
        return self.db.get(self.username)

    def update_user(self, updates):
        """If the item is updated, returns None. Otherwise, an exception is raised"""
        return self.db.update(updates, self.username)

    def delete_user(self):
        """Always returns None, even if the key does not exist"""
        return self.db.delete(self.username)

#insert_user('kamiltest', 'Kamil Testowy', '123fmas238j@#2')