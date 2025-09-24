import streamlit as st
import json

st.title("🧹 JSON Beautifier")

# --- Upload Section ---
st.subheader("Upload a JSON file")
uploaded_file = st.file_uploader("Choose a .json file", type="json")

file_json = None
if uploaded_file is not None:
    try:
        file_content = uploaded_file.read().decode("utf-8")
        file_json = json.loads(file_content)
        st.success("✅ File loaded successfully!")
    except Exception as e:
        st.error(f"❌ Failed to read file: {e}")

# --- Text Input Section ---
st.subheader("Or paste your JSON below")
raw_input = st.text_area("Paste your raw/minified JSON here:", height=200)

# --- Beautify Button ---
if st.button("Beautify"):
    if raw_input.strip():
        try:
            parsed_json = json.loads(raw_input)
            st.success("✅ Here's your beautified JSON:")
            st.json(parsed_json)
        except json.JSONDecodeError as e:
            st.error(f"❌ Invalid JSON from text:\n{e}")
    elif file_json:
        st.success("✅ Here's your beautified JSON from file:")
        st.json(file_json)
    else:
        st.warning("⚠️ Please paste JSON or upload a file to beautify.")
