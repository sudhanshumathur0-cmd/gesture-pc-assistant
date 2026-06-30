# frontend/app.py

import streamlit as st

st.set_page_config(
    page_title="AI Gesture Assistant",
    layout="wide"
)

st.title("🤖 AI Gesture Controlled PC Assistant")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Current Gesture")

    st.success("OPEN_PALM")

with col2:

    st.subheader("System Status")

    st.info("Running")

st.markdown("---")

st.subheader("Features")

st.write("✅ Hand Tracking")
st.write("✅ Gesture Detection")
st.write("✅ Browser Control")
st.write("✅ Screenshot Capture")
st.write("✅ Music Control")
