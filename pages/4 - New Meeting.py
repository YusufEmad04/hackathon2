import streamlit as st
import pandas as pd
import io
from PIL import Image
import base64

st.set_page_config(page_title="New Meeting") 

st.title("New Meeting")

# file = open("../images/peak logo.png", "rb")
# contents = file.read()
# img_str = base64.b64encode(contents).decode("utf-8")
# buffer = io.BytesIO()
# file.close()
# img_data = base64.b64decode(img_str)
# img = Image.open(io.BytesIO(img_data))
# resized_img = img.resize((150, 60))  # x, y
# resized_img.save(buffer, format="PNG")
# img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-repeat: no-repeat;
                padding-top: 50px;
                background-position: 50px 50px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "QIMA Meetings";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 50px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

audio , text, table = st.tabs(["Audio", "Text", "Table"])

with audio:
    col1, col2, col3 = st.columns([0.45, 0.10, 0.45])

    with col1:
        st.write("Record your voice:")
        voice_start_recording_button = st.button("Start Recording")
    with col3:
        st.write("Upload your meeting recording: ")
        uploaded_file = st.file_uploader(" ")


with text:
    text_area_text = st.text_area('Write something to be added to the meeting minute table', key='text_area_text')
    text_add_button = st.button('Add', key='text_add_button')

with table:
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
    # excel_add_button = st.button('Add', key='excel_add_button')


