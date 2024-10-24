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

st.set_page_config(page_title="App Mensagem Anônima", page_icon="💌")

def clear_text():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""

st.title('Enviar Mensagem Anônima 💌 🚀')

#st.image("logo.png")

st.markdown("""
**Escreva a mensagem no campo abaixo e clique em enviar.**
""")

mensagem = st.text_area('**Digite sua mensagem:**', height=200,  key='widget')


def enviar_email(mensagem):  
    corpo_email = mensagem

    msg = email.message.Message()
    msg['Subject'] = "Nova Mensagem Anônima - Antibullying"
    msg['From'] = 'mensagem_anonima_bullying@escolajayme.com'
    recipients = ["clyffe.assis@gmail.com", "clyffe.ribeiro@escolajayme.com"]
    msg['To'] = ",".join(recipients)
    password = 'ncmkfwsfzjgvkdkm' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], ["clyffe.assis@gmail.com", "clyffe.ribeiro@escolajayme.com", "mensagem_anonima_bullying@escolajayme.com", "denise.xavier@escolajayme.com"], msg.as_string().encode('utf-8'))
    


if st.button("Enviar"):
    try:
        enviar_email(mensagem)
        st.success(f'Mensagem Enviada Com Sucesso! 🚀')
        st.write("**Mensagem enviada:**")
        with st.container(border=True):            
            st.write(mensagem)
    except:
        st.error(f"Erro no envio da mensagem!")
