import smtplib

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("hydromoapp@gmail.com", "hydromoapp123")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("hydromoapp@gmail.com", "tomvaz11@gmail.com", message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")