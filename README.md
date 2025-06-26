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

## 🚀 Run the Application

From the project root:

```bash
py -3.9 -m streamlit run frontend/app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## ✅ Features

### Frontend (Streamlit)

- 📸 Upload invoice/receipt image (JPG, PNG)
- 📄 View extracted text via:
  - AWS Lambda-based OCR
  - Google Gemini Vision API
- 🧠 Extract structured **key-value data** from the image
- 💬 Ask questions (e.g., *"What is the PO number?"*) and get intelligent responses
- 📊 View parsed data in a table
- 📥 Export data to Excel with raw + structured sheets

### Backend

- Modularized for easy MLOps integration
- Uses `google.generativeai` for OCR and QA
- Backup fallback to `asprise` OCR API if needed
- Excel export using `pandas` and `openpyxl`

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

Install them using:

```bash
pip install -r requirements.txt
```