#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText 

body = """punyasloka pradhan"""
msg = MIMEText(body)

msg["From"] = 'punyasloka.pradhan@gmail.com'
msg["To"] = 'punyasloka.pradhan@gmail.com'
msg['Subject'] = 'sample mail'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('punyasloka.pradhan@gmail.com',"Sanju224855#")
server.send_message(msg)

print("Mail sent successfully")

server.quit()
