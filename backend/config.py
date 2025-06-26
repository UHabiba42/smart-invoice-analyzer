import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")
LAMBDA_OCR_URL = os.getenv("LAMBDA_OCR_URL")

#print(api_key)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# checking models

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)