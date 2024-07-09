import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd

# Initialize the DataFrame
if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=['Task', 'Status'])

def task_manager():
    st.title("To-Do List App")

    # Input new task
    new_task = st.text_input("Enter a new task")
    if st.button("Add Task"):
        if new_task:
            new_row = {'Task': new_task, 'Status': 'Incomplete'}
            st.session_state.tasks = pd.concat([st.session_state.tasks, pd.DataFrame([new_row])], ignore_index=True)
        else:
            st.warning("Please enter a task.")

    # Display tasks with AgGrid
    if not st.session_state.tasks.empty:
        gb = GridOptionsBuilder.from_dataframe(st.session_state.tasks)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children")
        gb.configure_column("Task", editable=True)
        gb.configure_column("Status", editable=True)
        gridOptions = gb.build()

        grid_response = AgGrid(
            st.session_state.tasks,
            gridOptions=gridOptions,
            data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            fit_columns_on_grid_load=True,
            enable_enterprise_modules=True,
            height=350,
            reload_data=True
        )

        selected = grid_response['selected_rows']
        if selected:
            st.write("Selected Tasks:")
            st.write(pd.DataFrame(selected))

        # Actions to complete or delete tasks
        if st.button("Mark Selected as Complete"):
            for selected_row in selected:
                index = st.session_state.tasks[st.session_state.tasks['Task'] == selected_row['Task']].index[0]
                st.session_state.tasks.at[index, 'Status'] = 'Complete'

        if st.button("Delete Selected Tasks"):
            for selected_row in selected:
                index = st.session_state.tasks[st.session_state.tasks['Task'] == selected_row['Task']].index[0]
                st.session_state.tasks = st.session_state.tasks.drop(index).reset_index(drop=True)
