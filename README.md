# Gemini Cover Letter Generator (Streamlit)

![Streamlit App](https://img.shields.io/badge/Built%20With-Streamlit-orange?style=flat-square)
![LLM-Powered](https://img.shields.io/badge/Powered%20by-Google%20Gemini-blue?style=flat-square)

This project is a **Cover Letter Generator** powered by the **Google Gemini LLM**. It allows users to generate professional, personalized cover letters based on:

- A job description (via LinkedIn job URL or pasted text)
- A resume (uploaded as PDF)
- Optional custom instructions (e.g., keep it short, anonymized, etc.)

The app is built using **Streamlit**, making it fast and interactive with a clean UI and custom styling.

---

## ✨ Features

- 🔗 Accepts LinkedIn Job URL or plain text job descriptions
- 📄 Accepts resume uploads in PDF format
- 🧠 Uses Gemini 1.5 Flash LLM to generate high-quality, relevant cover letters
- 📝 Generates downloadable `.docx` cover letters
- 🎨 Dark-themed and modern custom CSS interface
- 📦 Extracts job descriptions using headless Chrome and Selenium
- 🛡️ Error handling and user-friendly feedback

---

## 🖥️ Demo Screenshot

![App Screenshot](https://user-images.githubusercontent.com/your-screenshot-path/cover-letter-streamlit.png)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-cover-letter-generator-streamlit.git
cd gemini-cover-letter-generator-streamlit
```

### 2.💻 Setting Up a Virtual Environment (Windows)
Open Command Prompt (CMD) or PowerShell inside the project folder and run:

```bash
python -m venv venv
venv\Scripts\activate
```
Once the environment is activated, you’ll see (venv) in your terminal.

### 3. Install dependencies
We recommend using a virtual environment:

```bash
pip install -r requirements.txt
```
Additional setup:
Make sure you have Chrome and Chromedriver installed. You can install Chromedriver using:

```bash
sudo apt install chromium-chromedriver  # for Ubuntu/Debian
```
or download it manually from: https://chromedriver.chromium.org/downloads

Place it in your system PATH.

### 4. Set up Google Gemini API
Get your Google Gemini API key and paste it in the sidebar of the Streamlit app.

## 🔧 Running the App
```
streamlit run app.py
```
- Use the sidebar to enter your Gemini API key.
- Upload your resume (PDF).
- Enter job URL or description.
- Optionally add special instructions.
- Click Submit to generate the cover letter.
- The final .docx file will be saved in the generated-letters/ directory.

## 🗂️ Project Structure

├── app.py                        # Main Streamlit UI  
├── main.py                       # Core logic and response generation  
├── pdf_reader.py                
├── read_job_posting.py           
├── splitter.py                   
├── generated-letters/           
├── requirements.txt             
└── README.md
## 🛠️ Dependencies
- streamlit
- google-generativeai
- selenium
- beautifulsoup4
- python-docx
- PyPDF2
- langchain

## 💡 Future Improvements
- Add support for DOCX resumes
- Better URL text extraction with fallback scraping strategies
- Download button for generated letters
- OpenAI/Gemini model switch support

## 🤝 Contributing
Pull requests and ideas are welcome! Please open an issue to discuss changes or suggestions.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## ✉️ Contact
For questions or feedback, reach out via GitHub Issues or email me at heyitsmeakshayk@gmail.com