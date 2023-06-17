from langchain_utils import get_model
import streamlit as st

def button_callback(text):
    if text:
        try:

            text = "The following question is about the meeting minutes related to a certain company. Make sure to use reasoning in your answer. The CEO of the company will be asking you this question:\n" + text

            model = get_model()
            st.spinner("Thinking...")
            results = model.query(text, chain_type="refine")
            st.success("Done!")
            st.session_state["output"] = results
        except Exception as e:
            st.session_state["output"] = f"Something went wrong. Please try again. \n {e}"

    else:
        st.session_state["output"] = "Please enter a question."