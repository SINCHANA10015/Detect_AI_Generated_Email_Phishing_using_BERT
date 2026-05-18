import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

@st.cache_resource
def load_model():
    model = BertForSequenceClassification.from_pretrained('./final_model')
    tokenizer = BertTokenizer.from_pretrained('./final_model')
    return model, tokenizer

model, tokenizer = load_model()
model.eval()

st.title("🔐 Phishing Email Detector")
st.write("Fill in the email details below to check if it is phishing or legitimate.")

# ── Email Source Fields ──
st.subheader("📧 Email Source Information")
col1, col2 = st.columns(2)
with col1:
    sender_email = st.text_input("Sender Email", placeholder="example@domain.com")
    subject = st.text_input("Subject Line", placeholder="Enter email subject")
with col2:
    reply_to = st.text_input("Reply-To Email (if different)", placeholder="replyto@domain.com")
    sender_name = st.text_input("Sender Name", placeholder="Enter sender name")

# ── Email Body ──
st.subheader("📝 Email Content")
email_text = st.text_area("Email Body", height=200,
                          placeholder="Paste the full email content here...")

# ── Source Analysis Function ──
def analyze_source(sender_email, reply_to, subject):
    warnings = []
    score = 0

    if sender_email:
        domain = sender_email.split('@')[-1] if '@' in sender_email else ''
        suspicious_domains = ['gmail.com', 'yahoo.com', 'hotmail.com',
                              'outlook.com', 'live.com']
        if any(c.isdigit() for c in domain):
            warnings.append("⚠️ Sender domain contains numbers — suspicious!")
            score += 2
        if domain in suspicious_domains and sender_name:
            warnings.append(f"⚠️ Official organisation using free email ({domain}) — suspicious!")
            score += 2

    if sender_email and reply_to and reply_to.strip():
        sender_domain = sender_email.split('@')[-1] if '@' in sender_email else ''
        reply_domain = reply_to.split('@')[-1] if '@' in reply_to else ''
        if sender_domain != reply_domain:
            warnings.append("⚠️ Reply-To domain differs from Sender domain — high phishing risk!")
            score += 3

    if subject:
        urgent_keywords = ['urgent', 'verify', 'suspended', 'click', 'confirm',
                          'password', 'account', 'winner', 'free', 'limited',
                          'immediately', 'warning', 'alert', 'update required',
                          'expire', 'locked', 'unusual', 'unauthorized', 'refund',
                          'claim', 'congratulations', 'selected', 'prize']
        found = [kw for kw in urgent_keywords if kw.lower() in subject.lower()]
        if found:
            warnings.append(f"⚠️ Subject contains suspicious keywords: {', '.join(found)}")
            score += len(found)

    return warnings, score

# ── Check Button ──
if st.button("🔍 Check Email"):
    if email_text.strip() == "":
        st.warning("⚠️ Please enter the email content!")
    else:
        # BERT prediction
        inputs = tokenizer(email_text, return_tensors="pt",
                          truncation=True, max_length=128, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits).item()
        confidence = torch.softmax(outputs.logits, dim=1).max().item()

        # Source analysis
        warnings, source_score = analyze_source(sender_email, reply_to, subject)

        st.markdown("---")
        st.subheader("🔎 Analysis Results")

        # Source warnings
        if warnings:
            st.subheader("📌 Source Analysis")
            for w in warnings:
                st.warning(w)

        # BERT result
        st.subheader("🤖 Content Analysis (BERT)")
        if prediction == 0:
            bert_result = "PHISHING"
            st.error("🚨 BERT detected PHISHING content in the email body!")
        else:
            bert_result = "LEGITIMATE"
            st.success("✅ BERT detected LEGITIMATE content in the email body!")

        # ── Improved Confidence Formula ──
        bert_confidence = confidence * 100

        if bert_result == "PHISHING":
            # Boost confidence based on source risk score
            boost = source_score * 4  # each risk point adds 4%
            combined_confidence = min(bert_confidence + boost, 97.0)
        else:
            # For legitimate emails reduce confidence if source looks suspicious
            if source_score >= 3:
                combined_confidence = max(bert_confidence - (source_score * 3), 30.0)
            else:
                combined_confidence = bert_confidence

        # ── Final Verdict ──
        st.subheader("📋 Final Verdict")
        if bert_result == "PHISHING" or source_score >= 3:
            st.error(f"🚨 This email is likely PHISHING! (Confidence: {combined_confidence:.1f}%)")
        elif bert_result == "LEGITIMATE" and source_score == 0:
            st.success(f"✅ This email appears LEGITIMATE! (Confidence: {combined_confidence:.1f}%)")
        else:
            st.warning(f"⚠️ This email is SUSPICIOUS — treat with caution! (Confidence: {combined_confidence:.1f}%)")

        # Source risk score
        if source_score > 0:
            st.info(f"📊 Source Risk Score: {source_score}/10 — {'High Risk' if source_score >= 5 else 'Medium Risk'}")

        # ── Confidence Breakdown ──
        st.markdown("---")
        st.subheader("📈 Confidence Breakdown")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("BERT Confidence", f"{bert_confidence:.1f}%")
        with col2:
            st.metric("Source Risk Boost", f"+{min(source_score * 4, 37):.0f}%")
        with col3:
            st.metric("Combined Confidence", f"{combined_confidence:.1f}%")