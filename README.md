# 📧 Phishing Email Detection using BERT

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


