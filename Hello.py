import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config( page_title="Hello to QIMA", page_icon="👋", layout="wide",)

st.markdown("<h1 style='text-align: center;'>Welcome Back, Ahmed </h1>", unsafe_allow_html=True,help=False )
st.markdown("<h1 style='text-align: center;'> </h1>", unsafe_allow_html=True,help=False )

col1, col2 = st.columns([0.3,0.7])

with col1:

    st.markdown("<h5 style='text-align: center;'>Status Quo</h1>", unsafe_allow_html=True,help=False )

    labels = 'In Progress', 'Done', 'Overdue'
    sizes = [35, 15, 50]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)


with col2:

    st.markdown("<h5 style='text-align: center;'>Decision List</h1>", unsafe_allow_html=True,help=False )

    df = pd.DataFrame({
   'Meeting Title': ['Project Kickoff', 'Project Kickoff', 'Project Kickoff', 'Diversity and Inclusion', 'Diversity and Inclusion', 'Diversity and Inclusion', 'Process Improvement', 'Process Improvement', 'Process Improvement'],
   'Meeting Category': ['Project Management', 'Project Management', 'Project Management', 'Committee Meeting', 'Committee Meeting', 'Committee Meeting', 'Task Force Meeting', 'Task Force Meeting', 'Task Force Meeting'],
   'Decision': ['Establish project scope and timeline', 'Assign project roles and responsibilities', 'Set project milestones', 'Develop a diversity and inclusion training program', 'Identify potential barriers to inclusion', 'Establish diversity metrics', 'Analyze existing process and develop recommendations for improvement', 'Establish performance metrics to measure effectiveness of new process', 'Develop training program for new process implementation']
    })
    st.dataframe(
        df,
        column_config={
            "Meeting Title": "Meeting Title",
            "Decision" : st.column_config.Column(
            "Decision",
            # help="Streamlit **widget** commands 🎈",
            width="large",
            
        ),
        },
        hide_index=True,
    )

import io
from PIL import Image
import base64

file = open("images\peak logo.png", "rb")
contents = file.read()
img_str = base64.b64encode(contents).decode("utf-8")
buffer = io.BytesIO()
file.close()
img_data = base64.b64decode(img_str)
img = Image.open(io.BytesIO(img_data))
resized_img = img.resize((150, 60))  # x, y
resized_img.save(buffer, format="PNG")
img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url('data:image/png;base64,{img_b64}');
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