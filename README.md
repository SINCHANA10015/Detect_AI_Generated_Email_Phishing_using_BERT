# 📧Detect AI Generated Email Phishing using BERT (NLP . Deep Learning)              

![Python](https://img.shields.io/badge/Python-3.10-blue)
![BERT](https://img.shields.io/badge/Model-BERT-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-98.45%25-green)
![Platform](https://img.shields.io/badge/Platform-Kaggle-blue)

---

## 📌 Introduction

With the rise of AI-generated content, phishing emails have become 
increasingly sophisticated and harder to detect using traditional 
spam filters. Attackers now craft emails that closely mimic legitimate 
communication — making it nearly impossible for rule-based systems 
to catch them.

This project addresses that challenge by fine-tuning **BERT 
(Bidirectional Encoder Representations from Transformers)** — a 
state-of-the-art transformer model — to classify emails as either 
**Phishing** or **Legitimate** based on their content and source 
metadata.

BERT's bidirectional attention mechanism allows it to understand 
the full context of an email — not just keywords — making it far 
more effective than traditional machine learning approaches.

The system is deployed as an interactive web application using 
**Streamlit**, providing real-time phishing detection with confidence 
scores, source risk analysis, and detailed warnings.
---
## 🎯 Key Features

- 🤖 BERT-based deep learning email content classification
- 📧 Source metadata analysis (sender domain, reply-to, subject keywords)
- 📊 Combined confidence scoring (BERT + source risk boost)
- ⚠️ Real-time source risk warnings
- 🌐 Interactive Streamlit web interface
- 📈 Confidence breakdown display
- ✅ Tested on 20 real-world test cases

---

## 🖥️ Web Application Interface

The Streamlit app accepts the following inputs:

| Input Field | Purpose |
|-------------|---------|
| Sender Email | Checks domain for suspicious patterns |
| Reply-To Email | Detects domain mismatch |
| Subject Line | Scans for urgency keywords |
| Sender Name | Context for source analysis |
| Email Body | BERT deep content analysis |

### Output
- 🚨 **PHISHING** — Red alert with confidence score
- ✅ **LEGITIMATE** — Green result with confidence score  
- ⚠️ **SUSPICIOUS** — Yellow warning for borderline emails

---
## 📊 Model Performance

| Metric | Epoch 1 | Epoch 2 | Epoch 3 (Best) |
|--------|---------|---------|----------------|
| Accuracy | 97.0% | 97.4% | **98.45%** |
| Precision | 0.97 | 0.98 | **0.98** |
| Recall | 0.97 | 0.98 | **0.98** |
| F1-Score | 0.97 | 0.98 | **0.99** |
| Missed Phishing | 47 | 26 | **19** |

---

## 📁 Dataset

🔗 [Phishing Email Dataset — Kaggle](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)

| Detail | Value |
|--------|-------|
| Total Emails | 82,486 |
| Samples Used | 10,000 |
| Phishing | ~53% |
| Legitimate | ~47% |

---

## 🧠 Model Details

| Parameter | Value |
|-----------|-------|
| Base Model | bert-base-uncased |
| Total Parameters | 110 Million |
| Transformer Layers | 12 |
| Hidden Dimensions | 768 |
| Attention Heads | 12 |
| Max Token Length | 128 |
| Batch Size | 16 |
| Learning Rate | 2e-5 |
| Optimizer | AdamW |
| Training Platform | Kaggle GPU T4 x2 |
---
## 📂 Project Structure
Detect_AI_Generated_Email_Phishing_Detection/
├── Phishing_Email_Detection_using_BERT.ipynb
│     ├── Exploratory Data Analysis (EDA)
│     │     ├── Label Distribution
│     │     ├── Special Characters Analysis
│     │     ├── Top 20 Words in Phishing Emails
│     │     └── Word Cloud Visualization
│     ├── Data Preprocessing
│     │     ├── Lowercasing
│     │     ├── Stopword Removal
│     │     └── Label Encoding
│     ├── Train-Validation-Test Split (70/10/20)
│     ├── BERT Tokenization (max_length=128)
│     ├── Model Training (Epochs 1, 2, 3)
│     ├── Confusion Matrix and Classification Report
│     ├── Loss and Accuracy Graphs
│     └── Model Saving (save_pretrained)
├── app.py                 ← Streamlit web application
├── requirements.txt       ← Python dependencies
└── README.md              ← Project documentation
---
---

## 🛠️ Installation and Setup

```bash
# Step 1 — Clone the repository
git clone https://github.com/SINCHANA10015/Detect_AI_Generated_Email_Phishing_Detection.git
cd Detect_AI_Generated_Email_Phishing_Detection

# Step 2 — Install dependencies
pip install -r requirements.txt

# Step 3 — Download NLTK stopwords
python -c "import nltk; nltk.download('stopwords')"

# Step 4 — Download the trained model
# Train using the notebook on Kaggle OR
# Download final_model folder and place in project directory

# Step 5 — Run the web application
streamlit run app.py
```

---

## 🔄 System Workflow
User Input (Sender Email, Reply-To, Subject, Email Body)
|
+─────────────+─────────────+
|                           |
Source Analysis             BERT Analysis

Domain check              - Tokenization
Reply-To mismatch         - 12 Transformer layers
Subject keywords          - Softmax Classification
|                           |
+─────────────+─────────────+
|
Combined Confidence Score
BERT confidence + Source risk boost
|
+──────────────+──────────────+
|              |              |
PHISHING      LEGITIMATE     SUSPICIOUS
🚨 Red         ✅ Green       ⚠️ Yellow
---
---

## 💻 Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10 | Programming language |
| PyTorch | Latest | Deep learning framework |
| Hugging Face Transformers | Latest | BERT model and tokenizer |
| Streamlit | Latest | Web application frontend |
| Pandas | Latest | Data processing |
| NLTK | Latest | Text preprocessing |
| Scikit-learn | Latest | Metrics and data split |
| Matplotlib / Seaborn | Latest | Visualization |
| Kaggle | - | Cloud GPU training platform |

---

## 🔮 Future Work

- 🔲 Chrome Extension for real-time Gmail phishing detection
- 🔲 Train on full 82,486 email dataset with 5+ epochs
- 🔲 Gmail and Outlook API integration  
- 🔲 Microservices architecture (FastAPI + Streamlit)
- 🔲 URL and attachment scanning module
- 🔲 Deploy to Hugging Face Spaces for public access
- 🔲 Mobile application for on-the-go detection

---

## 👩‍💻 Author

**Sinchana Mutagekar**  
Department of Computer Science and Engineering  
Academic Year 2025-2026

---

## 📄 References

- Devlin et al. (2019) — BERT: Pre-training of Deep Bidirectional
  Transformers for Language Understanding. arXiv:1810.04805
- Hugging Face Transformers — https://huggingface.co
- Dataset — https://www.kaggle.com/datasets/naserabdullahalam/
  phishing-email-dataset
- Streamlit Documentation — https://docs.streamlit.io
