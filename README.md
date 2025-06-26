# ⚕️ Smart Invoice Analyzer – MLOps Final Project

A complete end-to-end system for uploading, reading, analyzing, and structuring invoice/receipt images using **OCR**, **Gemini AI**, and a Streamlit frontend. It supports both raw text extraction and structured key-value extraction, with Excel export and invoice-based question answering.

---

## 📂 Project Structure

```
smart-invoice-analyzer/
├── backend/
│   ├── ocr.py                # OCR logic using AWS Lambda and Gemini
│   ├── processor.py          # Processing & structuring invoice data
│   ├── excel_utils.py        # Save structured data to Excel
│   ├── gemini_qa.py          # Gemini-based QA system
│   └── config.py             # Environment configs and API keys
│
├── frontend/
│   └── app.py                # Streamlit interface
│
├── .env                      # Environment secrets (DO NOT COMMIT)
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview (this file)
└── .gitignore
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UHabiba42/smart-invoice-analyzer.git
cd smart-invoice-analyzer
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
LAMBDA_OCR_URL=https://your-aws-lambda-url/
```

---

## 📄 Detailed Docs

- 🔙 [Backend Documentation](backend/README.md)
- 🔜 [Frontend Documentation](frontend/README.md)


## Features

- Upload invoice images
- Extract text using AWS Lambda OCR & Gemini Vision API
- Structure key-value pairs
- Ask invoice-based questions
- Export data to Excel

---

## 📦 Dependencies

Key packages used:

- `streamlit`
- `pillow`
- `pandas`
- `requests`
- `google-generativeai`
- `openpyxl`
- `python-dotenv`