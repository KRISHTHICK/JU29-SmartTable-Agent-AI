import streamlit as st
from agent.table_reader import extract_tables_from_docx
from agent.pattern_finder import find_table_pattern
from agent.human_review import save_structure

st.set_page_config(page_title="SmartTable Agent", layout="wide")
st.title("🧠 SmartTable AI Agent – Extract Tables & Patterns from MS Word")

uploaded_file = st.file_uploader("Upload MS Word (.docx) Document", type=["docx"])

if uploaded_file:
    with open("temp.docx", "wb") as f:
        f.write(uploaded_file.read())

    tables = extract_tables_from_docx("temp.docx")
    
    if tables:
        for idx, table in enumerate(tables):
            st.subheader(f"Table {idx + 1}")
            pattern, df = find_table_pattern(table)
            st.dataframe(df)
            st.json(pattern)
            
            if st.button(f"✅ Approve Pattern for Table {idx + 1}"):
                save_structure(df, pattern)
                st.success("Pattern and data saved successfully.")
    else:
        st.warning("No tables found in the document.")
