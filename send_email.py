import smtplib, ssl  # standard library used as an emaillibrary
import os         # TO SECURE PASSWORD


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "priya.new456@gmail.com"
    # password = os.getenv("PASSWORD")
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = "priya.new456@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



