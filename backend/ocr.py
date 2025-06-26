from PIL import Image
from io import BytesIO
import logging
import os
from dotenv import load_dotenv
import logging
import google.generativeai as genai
import streamlit as st

load_dotenv()


FSDL_LAMBDA_OCR_URL = os.getenv("LAMBDA_OCR_URL")
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def send_image_to_lambda_ocr(image: Image.Image, lambda_url: str) -> str:
    """Simulate Lambda OCR call while using Gemini"""
    try:
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='PNG')
        logger.info(f"Simulating Lambda call to {lambda_url}")
        
        # Call real Gemini API here (to simulate result)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content([
            "Extract all text from this provided image (invoice). IMPORTANT: Do not rewrite or correct anything, just extract the text as-is.",
            image
        ])
        return response.text
    except Exception as e:
        logger.error(f"Simulated Lambda error: {str(e)}")
        return f"Error: Simulated Lambda failure - {str(e)}"
    

def get_image_text(image_file):
    try:
        #model = genai.GenerativeModel('gemini-1.5-flash-latest')
        img = Image.open(image_file)
        predicted_raw_text = send_image_to_lambda_ocr(img, FSDL_LAMBDA_OCR_URL)
        if predicted_raw_text.startswith("Error:"):
            st.error("Lambda OCR failed.")
            return None
        
        #response = model.generate_content(["Extract all text from this provided image (invoice), IMPORTANT: Do not rewrite and make corrections, just extract as it is data from the image", img])
        return predicted_raw_text
    except Exception as e:
        st.error(f"Gemini Vision failed: {str(e)}")
        return None
    

