import streamlit as st
import pandas as pd
# import speech_recognition as sr
from streamlit_option_menu import option_menu
import os
from streamlit_utils import *

if "output" not in st.session_state:
    st.session_state.output = ""

with st.sidebar:
    selected = option_menu("Qima Meeting", ["Ask", "Add", "Transcribe"], default_index=1)
    # selected

if selected == "Ask":
    st.header("Ask Qima Meetings")
    # st.write("This page is currently under construction...")
    input = st.text_area('Ask anything to the Qima existing meeting minute tables', key='ask_text_area')
    st.button('Ask', key='qima_ask_button', on_click=button_callback, args=(input,))
    st.write("Output:", st.session_state.output)

elif selected == "Add":
    st.header(f"Add Meeting Minutes")
    # st.write("This page is currently under construction...")

    # Create the tabs
    meeting_text, meeting_xlsx, meeting_voice = st.tabs(["Text", "Excel", "Voice"])

    # Content for meeting_text
    with meeting_text:
        st.text_area('write something to be added to meeting minute table', key='text_area_text')
        st.button('Add', key='text_add_button')

    # Content for meeting_xlsx
    with meeting_xlsx:
        # Create a file uploader widget
        uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

        # Check if a file was uploaded
        if uploaded_file is not None:
            try:
                # Read the uploaded Excel file
                df = pd.read_excel(uploaded_file)

                # Display the DataFrame
                st.dataframe(df)

                # save the uploaded file
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())

            except Exception as e:
                st.error("Error: Unable to load the file. Please make sure it is a valid Excel file. + " + str(e))

        else:
            st.info("Please upload an Excel file.")

        st.button('Add', key='excel_add_button')

    # Content for meeting_voice
    with meeting_voice:
        st.write("Record your voice:")
        if st.button("Start Recording"):
            # text = record_and_convert_audio()
            st.write("Transcription:")
            # st.write(text)

elif selected == "Transcribe":
    st.header("Transcribe Meeting Minutes")
    # st.write("This page is currently under construction...")
    st.write("Record your voice:")
    # if st.button("Start Recording"):
        # text2 = record_and_convert_audio()
        # st.write("Transcription:")
        # if not text2:
        #     st.write(text2)


