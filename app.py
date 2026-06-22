import streamlit as st

st.set_page_config(page_title="AI Resume Screener")

st.title("AI-Powered Resume Screening & Candidate Ranking System")

job_description = st.text_area(
    "Paste Job Description Here"
)

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze"):
    st.success(
        f"{len(uploaded_files)} resume(s) uploaded successfully."
    )

    st.write("Job Description:")
    st.write(job_description)
