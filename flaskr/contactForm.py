import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'campusparkingproject@gmail.com'
password = 'Park2020!'


def send_mail(text='', subject='', from_email='', to_email=''):

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText("<h1> This is working </H1>", 'plain')
    msg.attach(txt_part)

    msg_str = msg.as_string()
    # login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port='587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg_str)

    server.quit()
