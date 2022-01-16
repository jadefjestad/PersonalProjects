def send_email(message, sender_email, password, receiver_email, port=465, smtp_server="smtp.gmail.com"):
    # set up nice error messages if fields are empty?
    import smtplib, ssl
    import os

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    return True