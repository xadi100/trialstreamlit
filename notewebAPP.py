#here is the new:- 2

import streamlit as st

def main():
    st.set_page_config(page_title="Note Taking App", page_icon=":Notes:", layout="wide")
    st.title("Note Taking App")
    st.write("write here, what you want to store in the notes")

    # Get user input for a new note
    new_note = st.text_input("Add a new note:")
    add_button = st.button("Add Note")

    if add_button and new_note:
        # Store the new note in a session state variable (for demonstration purposes)
        add_note_to_session(new_note)
        st.success("Note added successfully!")

    # Display existing notes
    display_notes()

    # Delete note option
    if "notes" in st.session_state and st.session_state.notes:
        delete_note = st.number_input("Enter the number of the note to delete:", min_value=1, max_value=len(st.session_state.notes))
        delete_button = st.button("Delete Note")
        if delete_button and 1 <= delete_note <= len(st.session_state.notes):
            delete_note_from_session(delete_note - 1)
            st.success("Note deleted successfully!")
            st.experimental_rerun()  # Refresh the page

def add_note_to_session(note):
    # For demonstration purposes, we'll use session state to store notes
    if "notes" not in st.session_state:
        st.session_state.notes = []
    st.session_state.notes.append(note)

def delete_note_from_session(index):
    # For demonstration purposes, we'll use session state to store notes
    if "notes" in st.session_state:
        del st.session_state.notes[index]

def display_notes():
    # Display existing notes
    if "notes" in st.session_state and st.session_state.notes:
        st.subheader("Your Notes:")
        for i, note in enumerate(st.session_state.notes, start=1):
            st.write(f"{i}. {note}")
    else:
        st.info("No notes added yet.")

if __name__ == "__main__":
    main()
    
