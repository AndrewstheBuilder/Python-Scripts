import smtplib

receivers = ['rewstarverse@gmail.com']

message = """From: PWNED <yougot360@outlook.com>
To: <rewstarverse@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
address='yougot360@outlook.com'
password='YcCvJV7vpJNfPxf'
#set up SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.ehlo()
s.starttls()
s.login('yougot360@outlook.com', 'YcCvJV7vpJNfPxf')

try:
    s.sendmail(address, receivers, message)
    print("Successfully sent email")
    s.quit() #disconnect from SMTP server
except Exception:
    print()
