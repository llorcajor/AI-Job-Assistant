# 🤖 AI Job Application Assistant

This project is a complete, end-to-end automation suite that streamlines the job application process. It uses a series of Python scripts and AI agents to find job postings, generate tailored application documents, and track responses.

---

## Getting Started

Follow these steps to get the project running.

### Prerequisites

- Python 3.9+
- A Google Cloud account for the Gmail API
- A Google AI Studio account for the Gemini API

### Installation

1.  **Clone the repository (or download the files).**

2.  **Set up the Python virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Add API Keys and Credentials:**

    - **Gemini API Key:** Add your Google AI Studio API key to the `API_KEY` variable in `apply.py`.
    - **Gmail API Credentials:** Place your downloaded `credentials.json` file in the root project folder. You will be prompted to authenticate in your browser the first time you run the `email_checker.py` script.

5.  **Create Your Data Files:**
    - `master_resume.json`: Your complete professional history.
    - `knowledge_base.json`: Detailed STAR-method stories of your accomplishments.
    - `my_writing_style.txt`: 2-3 paragraphs of your own writing to guide the AI's tone.

---

## Usage

The main user interface is a Streamlit web application. To run it, execute the following command in your terminal:

```bash
streamlit run app.py
```
