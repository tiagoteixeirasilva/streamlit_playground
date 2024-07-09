import streamlit as st
from events import event_manager
from tasks import task_manager

def main():
    st.title("Life Organizer")
    
    menu = ["Home", "", "Goals", "Reminders", "Events"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to your Life Organizer app!")
        
    elif choice == "Tasks":
        st.subheader("Tasks")
        task_manager()
        
    elif choice == "Goals":
        st.subheader("Goals")
        goal_manager()

    elif choice == "Reminders":
        st.subheader("Reminders")
        reminder_manager()
        
    elif choice == "Events":
        st.subheader("Upcoming events")
        event_manager()


if __name__ == "__main__":
    main()
