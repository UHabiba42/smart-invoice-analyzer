import streamlit as st
import pandas as pd
from backend.processor import process_invoice, extraction
from backend.excel_utils import save_to_excel
from backend.gemini_qa import get_gemini_response
from backend.ocr import *

st.set_page_config(
        page_title="Smart Invoice Analyzer",
        page_icon="⚕️",
        layout="wide"
    )


# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4285F4;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: 500;
        }
        .header {
            color: #4285F4;
            font-weight: 700;
        }
        .receipt-card {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            color: #212529;
        }
    </style>
    """, unsafe_allow_html=True)


# Main App
def main():
    
    st.title("⚕️ Universal Invoice Reader & Processor")
    
    # Initialize session state
    if 'processed_receipts' not in st.session_state:
        st.session_state.processed_receipts = []
    
    # Upload and Process Section
    st.header("Upload Invoice or Receipt Image")
    uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(uploaded_file, caption="Uploaded Receipt", use_container_width=True)
            
        with col2:
            if st.button("Processing document..."):
                with st.spinner("Processing document..."):
                    try:
                        st.info("Using AWS Lambda-based OCR service for text extraction...")
                        ocr_result = process_invoice(uploaded_file)
                        #essential_data = extract_essential_data(ocr_result)
                        if ocr_result.get('success'):
                            receipt = ocr_result['receipts'][0]
                            ocr_text = receipt.get('ocr_text', '')
                            parsed_data = extraction(ocr_text)

                            if parsed_data:
                                invoice_data = {
                                    'file_name': ocr_result.get('file_name', uploaded_file.name),
                                    'ocr_confidence': receipt.get('ocr_confidence', 0),
                                    'parsed_data': parsed_data,
                                    'raw_text': ocr_text
                                }
                        
                        #if essential_data:
                            st.session_state.processed_receipts.append(invoice_data)
                            st.success("Invoice processed successfully!")
                            
                            # Display parsed data
                            with st.expander("View Extracted Data", expanded=True):
                                #st.json(essential_data['parsed_data'])
                                for key, value in parsed_data.items():
                                    st.write(f"**{key}**: {value}")
                            
                            # Save to Excel
                            if save_to_excel(st.session_state.processed_receipts):
                                st.success("Data saved to invoices.xlsx")
                                
                    except Exception as e:
                        st.error(f"Error processing order: {str(e)}")
    
    # Q&A Section
    if st.session_state.processed_receipts:
        st.header("Order Analysis")
        
        # Combine all parsed data for context
        context = "\n".join([str(receipt['parsed_data']) for receipt in st.session_state.processed_receipts])
        
        question = st.text_input("Ask a question about the invoices:")
        if question and st.button("Get Answer"):
            with st.spinner("Analyzing..."):
                response = get_gemini_response(question, context)
                st.markdown(f"""
                <div class="receipt-card">
                    <h4>Answer:</h4>
                    <p>{response}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # View All Data Section
    if st.session_state.processed_receipts:
        st.header("Processed Invoices")
        
        # Create DataFrame for display
        display_data = []
        for inv in st.session_state.processed_receipts:
            entry = {'File Name': inv['file_name'], 'OCR Confidence': f"{inv['ocr_confidence']:.1f}%"}
            entry.update(inv['parsed_data'])
            display_data.append(entry)
        
        st.dataframe(pd.DataFrame(display_data))
        
        # Download button
        with open("invoices.xlsx", "rb") as f:
            st.download_button(
                label="Download All Data (Excel)",
                data=f,
                file_name="invoices.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )



if __name__ == "__main__":
    main()