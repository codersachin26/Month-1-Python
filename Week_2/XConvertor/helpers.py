import hashlib
import logging
from zipfile import ZipFile
import os

import pdfplumber
import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "sk9625939@gmail.com"
sender_pass = "@Sachin#026K"
reciever = "sachin@codeops.tech"


def send_email(sender_email, sender_passwrd, receiver_email, zip_file, subject, body):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = zip_file  # In same directory as script

    # Open file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_passwrd)
        server.sendmail(sender_email, receiver_email, text)


def get_md5_hash(file):
    md5_obj = hashlib.md5()
    try:
        file = open(file)
        file_content = file.read()
        md5_obj.update(file_content.encode('utf-8'))
        file.close()
        return md5_obj.hexdigest()
    except OSError as err:
        logging.error(f'can not open {file} file, Error: {err}')
        return -1


def md5_checksum(data):
    md5_obj = hashlib.md5()
    md5_obj.update(data.encode('utf-8'))
    return md5_obj.hexdigest()


def md5_checksum_for_pdf(file):
    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        text_data = first_page.extract_text()
        md5 = hashlib.md5()
        md5.update(text_data.encode('utf-8'))
        return md5.hexdigest()


def zip_files(zip_file_name,files):
    zip_obj = ZipFile(zip_file_name, 'w')

    # Add multiple files to the zip
    for file in files:
        zip_obj.write(file)

    # close the Zip File
    zip_obj.close()
    return zip_file_name
