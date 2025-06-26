# 🎨 Frontend – Smart Invoice Analyzer (Streamlit UI)

This folder contains the **Streamlit-based frontend app** for the Smart Invoice Analyzer. It provides an easy-to-use UI to upload, analyze, and export invoice data.

---

## 📁 File Overview

```
frontend/
└── app.py          # Main Streamlit app interface
```

---

## 💡 Features

- 📤 Upload invoice images (JPG, PNG)
- 🔍 View raw OCR text from:
  - AWS Lambda
  - Google Gemini Vision API
- 🧠 View structured key-value invoice data
- 💬 Ask questions about the invoice (QA with Gemini)
- 📊 Display structured table
- 📥 Export to Excel

---

## ▶️ Run the App

From the **project root**, use:

```bash
py -3.9 -m streamlit run frontend/app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🔌 Dependencies

Handled via root `requirements.txt`, key ones include:

- `streamlit`
- `pillow`
- `pandas`
- `requests`
- `google-generativeai`

---

## 🔧 Troubleshooting

- Make sure `.env` is properly set up in the root.
- Ensure backend files are in the correct relative path.
- Use Python 3.9+ for best compatibility.