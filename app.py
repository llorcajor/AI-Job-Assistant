# app.py
import streamlit as st
from apply import run_application_process # Import the main function from your backend

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Job Application Assistant",
    page_icon="🤖",
    layout="centered"
)

# --- UI Elements ---
st.title("🤖 AI Job Application Assistant")
st.write("This tool automates the creation of tailored resumes and cover letters. Just provide the links and let the AI agents do the work.")

st.divider()

job_url = st.text_input(
    "1. Paste the Job Posting URL",
    placeholder="e.g., https://www.linkedin.com/jobs/view/..."
)
company_url = st.text_input(
    "2. Paste the Company's 'About Us' or 'Mission' URL",
    placeholder="e.g., https://www.company.com/about"
)

# --- Button to Trigger the Process ---
if st.button("Generate Application", type="primary"):
    if job_url and company_url:
        # Show a spinner while the backend is working
        with st.spinner("Working on it... This may take a few minutes..."):
            try:
                # Call the main logic from apply.py
                result = run_application_process(job_url, company_url)
                
                if result["success"]:
                    st.success(result["message"])
                    st.balloons()
                    
                    st.subheader("Generated Cover Letter Preview:")
                    # Use a text area to display the cover letter content
                    st.text_area("Cover Letter", value=result["cover_letter_text"], height=400)
                else:
                    st.error(result["message"])

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please provide both URLs before generating.")