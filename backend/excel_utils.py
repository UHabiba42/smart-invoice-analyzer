import pandas as pd
import streamlit as st

def save_to_excel(data_list, filename="invoices.xlsx"):
    try:
        summary_data = []
        raw_texts = []

        # 🔍 Collect all possible keys across invoices
        all_keys = set()
        for data in data_list:
            all_keys.update(data['parsed_data'].keys())

        for data in data_list:
            flat_data = {
                'File Name': data['file_name'],
                'OCR Confidence': f"{data['ocr_confidence']:.1f}%"
            }

            # Ensure all keys are represented (fill missing with blank)
            for key in all_keys:
                flat_data[key] = data['parsed_data'].get(key, "")

            summary_data.append(flat_data)

            raw_texts.append({
                'File Name': data['file_name'],
                'Raw Text': data['raw_text']
            })

        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='Extracted Data', index=False)
            pd.DataFrame(raw_texts).to_excel(writer, sheet_name='Raw Text', index=False)

        return True
    except Exception as e:
        st.error(f"Excel export failed: {str(e)}")
        return False