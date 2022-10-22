# This app is for grafical management of databases
import streamlit as st
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
from welcome_page import *
import streamlit_authenticator as stauth
import database as db
#users = db.fetch_all_users()
# AUTHORIZATION
# username: kamiltest
# password: 123#test


class Session:
    def __init__(self):
        #self.page_config = st.set_page_config(page_title="St for DB", page_icon="🧊", layout="wide")
        self.users = db.fetch_all_users()
        #
        self.usernames = [user["key"] for user in self.users]
        self.firstNames = [user["firstName"] for user in self.users]
        self.hashed_passwords = [user["password"] for user in self.users]
        self.credentials = self.generate_auth_credentials(usernames = self.usernames, names = self.firstNames, hashed_passwords = self.hashed_passwords)
        self.authentication = self.authenticate(self.credentials)
        self.authentication_status = self.authentication['authentication_status']
        self.name = self.authentication['name']
        self.username = self.authentication['username']
        # CURRENT
        

    def generate_auth_credentials(self, usernames, names, hashed_passwords):
        credentials = {"usernames":{}}
        for uname,name,pwd in zip(usernames,names,hashed_passwords):
            user_dict = {"name": name, "password": pwd}
            credentials["usernames"].update({uname: user_dict})
        # print(credentials)
        return credentials

    def authenticate(self, credentials):
        authentication_status = 0
        if authentication_status == 0:
            authenticator = stauth.Authenticate(credentials,"st_for_db", "#42$%", cookie_expiry_days=1)
            name, authentication_status, username   = authenticator.login('Login', 'main')
            if authentication_status == False:
                st.error("Username/password is incorrect")
                authentication_status = 0
            if authentication_status == None:
                st.warning("Please enter your username and password")
                authentication_status = 0
            if authentication_status:
                #placeholder.empty()
                #st.sucess('Sucessfully logged in')
                authentication_status = 1
                return name, authentication_status, username
        
        

class App(Session):
    def __init__(self, authentication_status, username, name):
        super().__init__(authentication_status, username, name)
        self.welcome_page = self.welcome_page(authentication_status = self.authentication_status, name = self.name)

    def welcome_page(self, authentication_status, name):
        if authentication_status == 1:
            st.set_page_config(page_title="St for DB", page_icon="🧊", layout="wide")
            st.title('noice, logged in')
            st.markdown(name)
        else:
            None

    placeholder = st.empty()
    #placeholder.info("CREDENTIALS | username:pparker ; password:abc123")





    