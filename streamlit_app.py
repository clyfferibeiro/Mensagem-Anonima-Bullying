""" 
If you've two-step verification enabled, your regular password won't work. Instead, generate an app-specific password:

- Go to your Google Account.
- On the left navigation panel, click on "Security."
- Under "Signing in to Google," select "App Passwords." You might need to sign in again.
- At the bottom, choose the app and device you want the app password for, then select "Generate."
- Use this app password in your Streamlit app.

"""

import streamlit as st
from email.mime.text import MIMEText
import smtplib
import email.message

st.title('Enviar Mensagem Anônima 💌 🚀')

st.markdown("""
**Escreva a mensagem no campo abaixo e clique em enviar.**
""")

mensagem = st.text_area('**Digite sua mensagem:**', height=200)

# # Taking inputs
# email_sender = st.text_input('From', 'clyffe.ribeiro@escolajayme.com', disabled=True)
# email_receiver = st.text_input('To')
# subject = st.text_input('Subject')
# body = st.text_area('Body')

# # Hide the password input
# password = st.text_input('Password', type="password", disabled=False)  

# if st.button("Send Email"):
#     try:
#         import smtplib, ssl

#     port = 465  # For SSL
#     #password = input("Type your password and press enter: ")

#     # Create a secure SSL context
#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#         server.login(email_sender, password)
#         # TODO: Send email here

#         st.success('Email sent successfully! 🚀')
#     except Exception as e:
#         st.error(f"Failed to send email: {e}")



def enviar_email(mensagem):  
    corpo_email = mensagem

    msg = email.message.Message()
    msg['Subject'] = "Nova Mensagem Anônima - Antibullying"
    msg['From'] = 'mensagem_anonima_bullying@escolajayme.com'
    msg['To'] = 'clyffe.ribeiro@escolajayme.com'
    password = 'ncmkfwsfzjgvkdkm' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    


if st.button("Enviar"):
    try:
        enviar_email(mensagem)
        st.success('Mensagem Enviada Com Sucesso! 🚀')
        with st.container():
            st.write("**Mensagem enviada:**")
            st.write(mensagem)
    except:
        st.error(f"Failed to send email: {e}")