import smtplib, ssl

from password import password, mail

sender = mail  # change mail to your email id
reciever = sender  # change sender to whom  you want to send the email
port = 465

message = """\
Subject: Python Email
This email is sent by python
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)  # change password to sender's email password
    server.sendmail(sender,reciever, message)


print('done')