from langchain_utils import get_model
import streamlit as st

def button_callback(text):
    if text:
        try:
            model = get_model()
            st.spinner("Thinking...")
            results = model.query(text, chain_type="refine")
            st.success("Done!")
            st.session_state["output"] = results["answer"]
        except Exception as e:
            st.session_state["output"] = f"Something went wrong. Please try again. \n {e}"