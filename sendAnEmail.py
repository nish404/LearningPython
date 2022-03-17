import smtplib

sender = "junkkmmail4100@gmail.com"
receiver = "junkkmmail4100@gmail.com"
password = "Chiken$123"
subject = "python email test"
body = "i wrote an email"

#header
#""" triple quotes can span multiple lines of text
message = f"""From: Sender{sender}
To: receiver{receiver}
Subject: {subject}\n
{body}

"""
#587 is the default mail submission port
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#if you receive an error you need to go into your account and turn on the LESS SECURE APP ACCESS setting
try:
    server.login(sender,password)
    print("logged in...")
    server.sendmail(sender,receiver,message)
    print("email has been sent")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")