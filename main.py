import subprocess
import sys
import streamlit as st


@st.cache_resource
def start_external_app():
    # Launches an external app (e.g., a background service or another script)
    # Using Popen allows it to run in the background without blocking Streamlit
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "fastapi_app:app", "--reload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return process


if __name__ == "__main__":
    external_process = start_external_app()
    tab1, tab2 = st.tabs(["docs", "redoc"])

    with tab1:
        st.header("http://127.0.0.1:8000/docs")
        st.iframe("http://127.0.0.1:8000/docs", height=1200, width=1200)

    with tab2:
        st.header("http://127.0.0.1:8000/redoc")
        st.iframe("http://127.0.0.1:8000/redoc", height=1200, width=1200)

    # no tabs
    # st.iframe("http://127.0.0.1:8000/docs", height=800, width=800) # default running http://127.0.0.1:8000
