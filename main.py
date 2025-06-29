from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
import os
from pdf_reader import load_pdf
from read_job_posting import extract_text_from_url
import google.generativeai as genai
import requests

def get_cover_letter(url, pdf, instructions, gemini_api_key):
    print("Get Cover Letter")
    
    # Load and process the user's resume and job posting text
    genai.configure(api_key=gemini_api_key)
    pdf_doc=""
    if pdf:
        pdf_doc = load_pdf(pdf)
        pdf_doc = "\n".join([page.page_content for page in pdf_doc])
    
    # Check if the URL is accessible or treat it as plain text
    job_post = ""
    try:
        print("Trying to get job info")
        job_post = extract_text_from_url(url)  # Extract text from URL if accessible
        if job_post==None:
            raise Exception("URL Not accessible")
    except Exception as e:
        print("Did not get job info")
        print(f"Error accessing URL: {e}. Treating URL as plain text.")
        job_post = url  # If URL is not accessible, treat it as plain text job description    
    
    if pdf and job_post:
        print("Pdf read ",job_post)
        pdf_doc+= job_post
    elif job_post:
        pdf_doc = job_post
    print("\n\n\nExtracted Information is: ",pdf_doc,"\n")
    
    # Setup Gemini model for QA
    def gemini_generate_cover_letter():
        print("Generate cover letter")
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        Write a professional cover letter based on the following information. You need to decide which parts are relevant with respect to the job description (will be given):
        
        {pdf_doc}.

        Always give me a letter only, dont give ask me questions as a response to this query
        Avoid hallucinating in large parts, you can hallucinate only when specific details (like a company name or equivalent) have to be manually added.          
        """
        if instructions:
            prompt += f"\nI have some special instructions for you: {instructions}"
        
        response = model.generate_content(prompt)
        return response.text.strip()

    # Define and run the query
    result = gemini_generate_cover_letter()
    print(result)
    return result
