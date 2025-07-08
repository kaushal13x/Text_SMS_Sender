import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Email Sender", page_icon="📧")
st.title("📨 Python Email Sender App")

receiver_email = st.text_input("Enter receiver email")
subject = st.text_input("Enter subject")
body = st.text_area("Enter email message")

sender_email = "alexalone939@gmail.com"
sender_password = "zzlq xlmf kfvp bhot"

if st.button("Send Email"):
    if receiver_email and subject and body:
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.set_content(body)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
    else:
        st.warning("⚠️ Please fill out all fields.")
