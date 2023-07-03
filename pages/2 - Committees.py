import streamlit as st
import pandas as pd
import io
from PIL import Image
import base64

st.set_page_config(page_title="Committees") 

st.title("Your Committees")

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

Marketing , Finance , DiversityandInclusion, HealthandWellness   = st.tabs(["Marketing Committee", "Finance Committee", "Diversity and Inclusion Committee", "Health and Wellness Committee" ])

with Marketing:
    st.markdown("<h7 style='text-align: center;'> </h3>", unsafe_allow_html=True,help=False )
    st.markdown("<h3 style='text-align: center;'>Marketing Committee</h3>", unsafe_allow_html=True,help=False )
    st.markdown("<h7 style='text-align: center;'> </h3>", unsafe_allow_html=True,help=False )

    col1, col2, col3 = st.columns([0.65, 0.10, 0.25])

    with col1:

        campaign_data = {
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'],
        'Click-through Rate': [0.05, 0.07, 0.08, 0.06, 0.09],
        'Conversion Rate': [0.02, 0.03, 0.04, 0.03, 0.05]
        }
        campaign_df = pd.DataFrame(campaign_data)

        # Create a bar chart of the performance metrics
        st.write("Advertising Campaign Performance Metrics")
        st.bar_chart(campaign_df.set_index('Week'))

        st.markdown("<h5 style='text-align: center;'>Potential decisions:</h5>", unsafe_allow_html=True,help=False )
        st.markdown("- Develop a new advertising campaign.")
        st.markdown("- Rebrand the company logo.")
        st.markdown("- Increase social media presence.")
        st.markdown("- Conduct market research to identify new customer segments.")

    with col3:
        st.markdown("<h5 style='text-align: center;'>Next Meeting:</h5>", unsafe_allow_html=True,help=False )
        st.markdown("<h7 style='text-align: center;'>Topics:</h7>", unsafe_allow_html=True,help=False )
        st.markdown("- Review the results of the latest advertising campaign.")
        st.markdown("- Brainstorm ideas for a new campaign.")
        st.markdown("- Evaluate the effectiveness of the current social media strategy.")

        text_area_text = st.text_area('Ask QIMA about this meeting', key="text_area")
        text_add_button = st.button('Ask',key="btn")
        
with Finance:

    st.markdown("<h7 style='text-align: center;'> </h3>", unsafe_allow_html=True,help=False )
    st.markdown("<h3 style='text-align: center;'>Finance Committee</h3>", unsafe_allow_html=True,help=False )
    st.markdown("<h7 style='text-align: center;'> </h3>", unsafe_allow_html=True,help=False )

    col1, col2, col3 = st.columns([0.65, 0.10, 0.25])

    with col1:

        st.write("Finance Performance Metrics")
        social_data = {
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'Engagement': [1000, 1500, 1200, 2000, 1800]
        }
        social_df = pd.DataFrame(social_data)

        # Create a line chart of the social media engagement over time
        st.line_chart(social_df.set_index('Date'), width=0, height=0, use_container_width=True)


        st.markdown("<h5 style='text-align: center;'>Potential decisions:</h5>", unsafe_allow_html=True,help=False )
        st.markdown("- Develop a new budgeting strategy.")
        st.markdown("- Implement a risk management plan.")
        st.markdown("- Create a financial plan for the next quarter.")
        st.markdown("- Invest in new technology.")

    with col3:
        st.markdown("<h5 style='text-align: center;'>Next Meeting:</h5>", unsafe_allow_html=True,help=False )
        st.markdown("<h7 style='text-align: center;'>Topics:</h7>", unsafe_allow_html=True,help=False )
        st.markdown("- Review the results of the latest advertising campaign.")
        st.markdown("- Brainstorm ideas for a new campaign.")
        st.markdown("- Evaluate the effectiveness of the current social media strategy.")

        text_area_text1 = st.text_area('Ask QIMA about this committee"s meetings')
        text_add_button1 = st.button('Ask',key="btn1")
        
with DiversityandInclusion:

    st.markdown("<h7 style='text-align: center;'> </h3>", unsafe_allow_html=True,help=False )
    st.markdown("<h3 style='text-align: center;'>Diversity and Inclusion Committee</h3>", unsafe_allow_html=True,help=False )
    st.markdown("<h7 style='text-align: center;'> </h3>", unsafe_allow_html=True,help=False )

    col1, col2, col3 = st.columns([0.65, 0.10, 0.25])

    with col1:

        st.write("Finance Performance Metrics")
        social_data = {
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'Engagement': [1000, 1500, 1200, 2000, 1800]
        }
        social_df = pd.DataFrame(social_data)

        # Create a line chart of the social media engagement over time
        st.line_chart(social_df.set_index('Date'), width=0, height=0, use_container_width=True)


        st.markdown("<h5 style='text-align: center;'>Potential decisions:</h5>", unsafe_allow_html=True,help=False )
        st.markdown("- Develop a new budgeting strategy.")
        st.markdown("- Implement a risk management plan.")
        st.markdown("- Create a financial plan for the next quarter.")
        st.markdown("- Invest in new technology.")

    with col3:
        st.markdown("<h5 style='text-align: center;'>Next Meeting:</h5>", unsafe_allow_html=True,help=False )
        st.markdown("<h7 style='text-align: center;'>Topics:</h7>", unsafe_allow_html=True,help=False )
        st.markdown("- Review the results of the latest advertising campaign.")
        st.markdown("- Brainstorm ideas for a new campaign.")
        st.markdown("- Evaluate the effectiveness of the current social media strategy.")

        text_area_text2 = st.text_area('Ask QIMA about this meeting', key="text_area2")
        text_add_button2 = st.button('Ask', key="btn2")
    

with HealthandWellness:
    st.write("Recordss your voice:")

