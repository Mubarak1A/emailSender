#!/usr/bin/python3
"""
    Email Sender Script
    Sends emails to a list of recipients.

    This script establishes a connection with the SMTP server 
    and creates an email message using the EmailMessage class. 
    The content of the email is read from an HTML file and substituted with a variable value. 
    The function then sends the email using the SMTP server.

    Args:
    None

    Outputs:
    None

    Example Usage:
    python3 send_mail.py

    """

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

emails = [] #list suppose contain list of emails to send mail to

#looping through emails to send mail
for a_email in emails:
    html = Template(Path("./sample.html").read_text())
    email = EmailMessage()
    email['from'] = 'SENDER NAME HERE'
    email['to'] = 'RECUEVER EMAIL'
    email['subject'] = 'MAIL SUBJECT HERE'

    email.set_content(html.substitute(name = 'NAME (MIGHT BE ANY OTHER VARIABLE ARGUMENT)'), 'html')

# the smtplib guide...(Simple Mail Transfer Protocol lib)
    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('SENDER EMAIL', 'SENDER PASSWORR')
        smtp.send_message(email)

        print(f'Mail Sent to {a_email} successfully!')
