import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# WHOLE PART TO CHANGE INTO CLASS

def sql_table_editor():

    #st.sidebar.selectbox('Pick one', ['cats', 'dogs'])

    #title = st.title('SQL table editor')
    todo_options = ['Insert', 'Update', 'Delete']
    
    def database_connection():
        #connection_string = st.sidebar.text_input('Connection String')
        

        tab1, tab2 = st.sidebar.tabs(["Connection", "Table"])

        with tab1:
            saved_connections = ['MyConnection', 'WINSRVSSRS Report Team']
            connection_data = st.selectbox("Insert or choose your connection string", saved_connections, 1)
            col1, col2 = st.columns(2)
            with col1:
                database_type = st.selectbox("Choose DB type", ['SQL Server','PostgeSQL'], 0)
                database_login = st.selectbox("DB Login", ['SqlWarior420','XXXD/Domain User'], 0)
            with col2:
                database_api = st.selectbox("Choose DB API", ['ODBC','PostgeSQL'], 0)
                database_password = st.text_input("Password ", type="password")
            
            col1_button, col2_button = st.columns(2)
            with col1_button:
                btn_test_connetion = st.button('Test connection')
                
            with col2_button:
                btn_save_connetion = st.button('Save connection')
        if btn_test_connetion:
            st.sidebar.success('Connection sucessfully established')
        with tab2:

            av_databases = ['Shows', 'ReportGeeks']
            chosen_database = st.selectbox("Insert or choose database", av_databases, 0)
            av_tables = ['Netflix shows', 'Numbers']
            chosen_table = st.selectbox("Insert or choose table", av_tables, 0)
        


    db_conn = database_connection()

        
    def table_editor():
        
        # DATA
        data = pd.read_csv('pages_selectbox/netflix_titles.csv')
        data_columns = data.columns
        #[['show_id', 'type', 'title', 'release_year', 'duration']]
        
        with st.form(key = 'table_form'):
            col1, col2, col3 = st.columns([4,4,2])
            with col1:
                crud_action = st.selectbox("First choose what you want to do", todo_options, 1)
                #columns_selection = st.mu
            with col2:
                # ST WIDGETS - uncomment to use of if need, search ###3### to find the other places where to replace code
                #default = data_columns[2]
                col_to_edit = st.multiselect('Choose columns you want to edit', options=data_columns, default=['title', 'type', 'director'])
                col_index = data_columns[0]
                

                def append_list(a, b):
                    c = []
                    if type(a) != list:
                        a = [a]
                    if type(b) != list:
                        b = [b]
                    for arg in a:
                        c.append(arg)
                    for arg in b:
                        c.append(arg)
                    return c 

                columns_to_compare = append_list(col_index, col_to_edit)

            with col3:
                
                selection_mode = st.radio('Selection Type', options = ['single','multiple'])
            st.form_submit_button('Confirm your selections')

        # GRID CONFIG
        gd = GridOptionsBuilder.from_dataframe(data)
        gd.configure_pagination(enabled=True)
        gd.configure_default_column(editable = False, groupable = False)
        for column in col_to_edit:
            gd.configure_column(column, header_name=column, editable=True)
        #gd.configure_selection(selection_mode='single', use_checkbox= False)###3###
        gd.configure_selection(selection_mode=selection_mode, use_checkbox= True)

        gridoptions=gd.build()
        #_selectedRowNodeInfo
        dataGrid = AgGrid(data, gridOptions=gridoptions,
                        #update_mode=GridUpdateMode.SELECTION_CHANGED,
                        height = 500,
                        allow_unsafe_jscode=True,
                        theme='streamlit'
                        )

        v = dataGrid['selected_rows']

        def crud_action_manage():
            if crud_action == todo_options[0]:
                st.write(todo_options[0])
            if crud_action == todo_options[1]:
                st.write(todo_options[1])
        if v:
            st.markdown('DATA AFTER CHANGES')
            v_pd = pd.DataFrame(v)
            v_pd = v_pd.iloc[: , 1:].copy()
            v_pd = v_pd[columns_to_compare]
            st.dataframe(v_pd)

           #st.write('Please review changes you want to make')
            ids = v_pd['show_id'].tolist()
            st.markdown('ORIGINAL DATA')
            v_pd_original_mask = data['show_id'].isin(ids)
            v_pd_original = data.loc[v_pd_original_mask]
            v_pd_original = v_pd_original[columns_to_compare]
            st.dataframe(v_pd_original)


            
                # HERE TO IMPLEMENT SQL ALCHEMY
        x = "UPDATE dbo.SomeTable SET type = X  WHERE ID = Y" 
        #st.write(x)
        dfs = pd.DataFrame(v)

        if st.button('Update in db'):
            st.markdown(x)
            st.write('do tego audyt na sql albo z sqlalchemy')
        else:
            st.write('Click on the button if you want to commit your update')


    db_editor = table_editor()

