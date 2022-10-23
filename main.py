import streamlit as st
import streamlit_authenticator as stauth
from database import deta_db
from pages_selectbox.welcome_page import *
from pages_selectbox.SQL_tables_editor import *

#kamiltest
#123#test

def app_general_settings():
    st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

app_settings = app_general_settings()

class Authentication:
    # THIS CLASS IS FOR MANAGING AUTHENTICATION 
    def __init__(self, users_table):
        self.users_table = users_table
        self.auth_list = self.auth_lists(users = self.users_table, username='key', name='name', password='password')
        self.credentials = self.auth_credentials(self.auth_list[0],self.auth_list[1],self.auth_list[2])
        self.authentication = self.authenticate(self.credentials)
        self.authentication_status = self.authentication[2]
        self.authenticator = self.authentication[0]
        self.user_key=  self.authentication[3]
        self.user_name = self.authentication[1]

    def auth_lists(self, users, username, name, password):
        usernames = [user[username] for user in users]
        names = [user[name] for user in users]
        hashed_passwords = [user[password] for user in users]
        return usernames, names, hashed_passwords

    def auth_credentials(self, usernames, names, hashed_passwords):
        credentials = {"usernames":{}}
        for uname,name,pwd in zip(usernames,names,hashed_passwords):
            user_dict = {"name": name, "password": pwd}
            credentials["usernames"].update({uname: user_dict})
        return credentials

    def authenticate(self, credentials):
        authenticator = stauth.Authenticate(credentials,"SfinanceKamil", "k3Y423a", cookie_expiry_days=1)
        name, authentication_status, username = authenticator.login('Login', 'main')
        return authenticator, name, authentication_status, username

users = deta_db.fetch_all_users()
Auth = Authentication(users)
# username: kamiltest
# password: 123#test

#placeholder = st.empty()

class Application():
    def __init__(self, user_key, user_name):
        
        self.welcome = st.sidebar.title('Welcome ' + user_name)
        self.logout = Auth.authenticator.logout("Logout", "sidebar")
        #
        self.av_pages = ['Welcome', 'SqlEditor']
        self.current_page_selectbox = st.sidebar.selectbox("Select a page", self.av_pages, 0)
        self.line_separator = st.sidebar.write('---')

        self.current_page = self.current_page(self.current_page_selectbox, self.av_pages)

    def current_page(self, current_page, av_pages):
        if current_page == av_pages[0]:
            page = welcome_page()
        if current_page == av_pages[1]:
            page = sql_table_editor()


    # WELCOME PAGE

if st.session_state['authentication_status'] == False:
    st.error("Username/password is incorrect")

if st.session_state['authentication_status'] == None:
    st.info("Please enter your username and password")

if st.session_state['authentication_status']:
    App = Application(Auth.user_key, Auth.user_name)
    


# placeholder.empty()

# # username: kamiltest
# # password: 123#test
# st.success('Done!')
# st.title('st.session_state[name]:'+st.session_state['name'] )
# Auth.authenticator.logout("Logout")#