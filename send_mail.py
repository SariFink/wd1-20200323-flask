import smtplib

# enable google mails from apps:
# https://myaccount.google.com/lesssecureapps
# https://support.google.com/accounts/answer/6010255

gmail_user = 'wondermessage4you@gmail.com'
gmail_password = '123abc!!!'

# And imghdr to find the types of our images
import imghdr

# Here are the email package modules we'll need
from email.message import EmailMessage

# Create the container email message.
msg = EmailMessage()
msg['Subject'] = 'OMG Super Important Message'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = 'wondermessage4you@gmail.com'
msg['To'] = ', '.join(['fink.sari@gmail.com'])
msg.set_content("Great text! Try to change this")
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

# Open the files in binary mode.  Use imghdr to figure out the
# MIME subtype for each specific image.
with open('cat.jpg', 'rb') as fp:
    img_data = fp.read()
    msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

# Send the email via our own SMTP server.
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
