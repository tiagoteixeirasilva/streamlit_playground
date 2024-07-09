import streamlit as st
import pandas as pd
from events_database import init_db, add_event, get_events, delete_event

init_db()

def event_manager():
    # Display custom events in a table
    st.write("### Your Events")
    events = get_events()
    if events:
        df_events = pd.DataFrame(events, columns=["ID", "Name", "Date", "Time", "Link"])
        st.table(df_events)
        for event in events:
            event_id, name, date, time, link = event
            if st.button(f"Delete Event {event_id}", key=event_id):
                delete_event(event_id)
                st.success("Event deleted successfully!")
                st.experimental_rerun()
    else:
        st.write("There are no upcoming events.")


    # Form to add new event
    st.write("### Add events")

    with st.form(key="event_form"):
        event_name = st.text_input("Event Name")
        event_date = st.date_input("Event Date")
        event_time = st.time_input("Event Time")
        event_link = st.text_input("Event Link (optional)")
        
        submit_button = st.form_submit_button(label="Add Event")
        
        if submit_button:
            add_event(event_name, event_date.strftime('%Y-%m-%d'), event_time.strftime('%H:%M:%S'), event_link)
            st.success("Event added successfully!")