import json
import requests
import google.generativeai as genai
import streamlit as st
from ocr import get_image_text
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def parse_implant_data(ocr_text):
#     """Parse the OCR text into structured key-value pairs"""
#     data = {}
    
#     # Extract PO Number
#     po_match = re.search(r'PO\s+(\w+)', ocr_text)
#     if po_match:
#         data['PO_Number'] = po_match.group(1)
    
#     # Extract Lot Number
#     lot_match = re.search(r'Lot\s+([\w\.]+)', ocr_text)
#     if lot_match:
#         data['Lot_Number'] = lot_match.group(1)
    
#     # Extract Expiration Date
#     exp_match = re.search(r'Exp\. Date\s+([\d-]+)', ocr_text)
#     if exp_match:
#         data['Expiration_Date'] = exp_match.group(1)
    
#     # Extract Implant Details
#     implant_lines = [line for line in ocr_text.split('\n') if 'D.L51' in line]
#     for line in implant_lines:
#         parts = re.split(r'\s{2,}', line.strip())
#         if len(parts) >= 4:
#             level = parts[0]
#             data[f'Level_{level}_Minus'] = parts[1]
#             data[f'Level_{level}_Plan'] = parts[2]
#             data[f'Level_{level}_Plus'] = parts[3]
#             if len(parts) > 4:
#                 data[f'Level_{level}_Screws'] = parts[4]
    
#     # Extract Entered By and Date
#     entered_match = re.search(r'Entered By\s+([\w\s]+)\n\s+Date\s+([\w\s]+)', ocr_text)
#     if entered_match:
#         data['Entered_By'] = entered_match.group(1).strip()
#         data['Entry_Date'] = entered_match.group(2).strip()
    
#     return data

# def extract_essential_data(ocr_result):
#     """Extract and structure the essential data"""
#     try:
#         print(ocr_result.get("receipts"))
#         receipt = ocr_result['receipts'][0]
#         ocr_text = receipt.get('ocr_text', '')
        
#         # Parse the structured data from OCR text
#         parsed_data = parse_implant_data(ocr_text)
        
#         return {
#             'file_name': ocr_result.get('file_name', ''),
#             'merchant_name': receipt.get('merchant_name', ''),
#             'merchant_address': receipt.get('merchant_address', ''),
#             'ocr_confidence': receipt.get('ocr_confidence', 0),
#             'parsed_data': parsed_data,
#             'raw_text': ocr_text  # Keep raw text for reference
#         }
#     except Exception as e:
#         st.error(f"Error processing receipt data: {str(e)}")
#         return None

def process_invoice(image_file):
    url = "https://ocr.asprise.com/api/v1/receipt"
    res = requests.post(url,
                      data = {'api_key': 'TEST', 'recognizer': 'auto', 'ref_no': 'oct_python_123'},
                      files = {'file': image_file},
                      timeout=60)
    result = json.loads(res.text)
        
    if result.get('success', False):
        return result
    
    ocr_text = get_image_text(image_file)
    if ocr_text:
        return {
                'success': True,
                'receipts': [{
                    'ocr_text': ocr_text,
                    'ocr_confidence': 90
                }],
                'file_name': image_file.name
            }
    else:
        return {'success': False, 'message': 'All processing methods failed'}
    

def extraction(ocr_text):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        prompt = f"""
        Analyze this invoice or receipt text and extract all useful fields in key-value format.
        The output should be valid JSON.
        Important: Make key- value words as it is same from the analyzed text, do not alter the words or make corrections by yourself, your task is only to structured the data in key-value format. All fields as columns and their filled answers as keys, otherwise only extract values with Unk Key.

        Document Text:
        {ocr_text}

        Return ONLY valid JSON.
        """
        response = model.generate_content(prompt)
        
        # Extract JSON from response
        json_str = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(json_str)
    except Exception as e:
        st.error(f"Gemini extraction failed: {str(e)}")
        return None