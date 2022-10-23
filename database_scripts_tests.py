#import streamlit_authenticator as stauth
from database import *
#import database as db



users_insert = users_database('first tester', 'firstNme', 'lastName', 'password123$', 'emailTest@123.xd')
users_insert.insert_user()

#for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
#    db.insert_user(username, name, hash_password)