import google.generativeai as genai
import os
from dotenv import load_dotenv


# Configure Google Gemini AI
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, context):
    """Get response from Gemini AI"""
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt = f"""
    You are an invoices reader specialist assistant. Analyze this invoice data:
    {context}
    
    Question: {question}
    
    Provide a detailed, professional response based on the data.
    """
    response = model.generate_content(prompt)
    print(response.text)
    return response.text