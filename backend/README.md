# 🧠 Backend – Smart Invoice Analyzer

This folder contains the core logic for OCR, data structuring, invoice analysis, Excel export, and question answering powered by **Gemini AI**.

---

## 🧾 Files Overview

```
backend/
├── ocr.py                # OCR logic using AWS Lambda and Gemini
├── processor.py          # Processing & structuring invoice data
├── excel_utils.py        # Save structured data to Excel
├── gemini_qa.py          # Gemini-based QA system
└── config.py             # Environment configs and API keys
```

---

## ⚙️ Functionality

- **OCR Extraction**
  - Uses AWS Lambda for OCR
  - Fallback: Google Gemini Vision API
- **Data Structuring**
  - Extracts key fields from raw invoice text
- **Excel Export**
  - Creates downloadable Excel files with raw + structured data
- **Invoice QA**
  - Ask questions like *"What is the invoice date?"*

---

## 📦 Requirements

Ensure the following are installed (handled via root `requirements.txt`):

```bash
pip install pandas requests openpyxl google-generativeai python-dotenv
```

OR Install them using:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Stored in `.env`:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
LAMBDA_OCR_URL=https://your-aws-lambda-url/
```

These are accessed via `config.py`.

---

## Usage

All backend modules are imported and used inside the Streamlit frontend app. To test them independently, you can write simple test scripts or unit tests.

---

## 🧪 Testing

You can test individual components:

```python
from ocr import extract_text_lambda
from processor import extract_key_values
from excel_utils import save_to_excel
```