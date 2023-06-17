import streamlit as st
import pandas as pd
# import speech_recognition as sr
from streamlit_option_menu import option_menu
import os
from streamlit_utils import *

# def record_and_save_audio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Speak now...")
#         audio = r.listen(source)
#
#     try:
#         text = r.recognize_google(audio)
#         st.session_state['recorded_text'] += text
#     except sr.UnknownValueError:
#         st.write("Unable to recognize speech.")
#     except sr.RequestError as e:
#         st.write(f"Error: {e}")

if "output" not in st.session_state:
    st.session_state.output = ""

if "text_area_text" not in st.session_state:
    st.session_state.text_area_text = ""

with st.sidebar:
    selected = option_menu("Qima Meeting", ["Ask", "Add", "Transcribe", "Your meetings"], default_index=0)
    # selected

if selected == "Ask":
    # st.header("Ask Qima Meetings")
    st.markdown("<h1 style='text-align: center;'> Ask QIMA Meetings </h1>", unsafe_allow_html=True)
    # st.write("This page is currently under construction...")
    input = st.text_area('Ask anything to the Qima existing meeting minute tables', key='ask_text_area', value=st.session_state.text_area_text)
    st.session_state.text_area_text = input
    st.button('Ask', key='qima_ask_button', on_click=button_callback, args=(input,))
    if st.session_state.output:
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
        st.write("Upload an MP3 or WAV file:")
        uploaded_voice_file = st.file_uploader("Upload Voice File", type=["mp3", "wav"])
        if st.button("Add", key="voice_add_button"):
            if uploaded_voice_file is not None:
                st.write("Input stored:", uploaded_voice_file)
            else:
                st.warning("Please upload an MP3 or WAV file.")

elif selected == "Transcribe":
    # st.header("Transcribe Meeting Minutes")
    # # st.write("This page is currently under construction...")
    # st.write("Record your voice:")
    # # if st.button("Start Recording"):
    #     # text2 = record_and_convert_audio()
    #     # st.write("Transcription:")
    #     # if not text2:
    #     #     st.write(text2)
    st.header("Transcribe Meeting Minutes")
    st.write("Record your voice:")
    recording_button = st.button("Start/Stop Recording")
    # if recording_button:
    #     if not st.session_state.get('recording', False):
    #         st.session_state['recording'] = True
    #         st.write("Recording started.")
    #         st.session_state['recorded_text'] = ""
    #         # record_and_save_audio()
    #     else:
    #         st.session_state['recording'] = False
    #         st.write("Input stored:", st.session_state['recorded_text'])

elif selected == "Your meetings":
    st.header("Your Meetings")
    # st.write("This page is currently under construction...")
    st.write("Your meetings:")
    # load dummy data csv with pandas
    df = pd.read_csv("Dummy minutes.csv")
    # display the data
    st.dataframe(df)


