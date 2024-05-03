import requests
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # 邮件设置
    mail_content = "太好啦: ahr999_index小于1.2，速速定投！！！"
    sender_address = os.environ['SENDER_EMAIL']
    sender_pass = os.environ['SENDER_PASSWORD']
    receiver_address = os.environ['RECEIVER_EMAIL']

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'AHR999 Index Alert'   #The subject line
    message.attach(MIMEText(mail_content, 'plain'))

    #Use QQ's smtp server to send email.
    session = smtplib.SMTP_SSL('smtp.qq.com', 465) #use QQ with port
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

def check_ahr999_index():
    response = requests.get('http://43.129.241.254:5000/info/')
    ahr999_index = float(response.json()['ahr999'])
    if ahr999_index < 1.2:
        send_email()

if __name__ == "__main__":
    check_ahr999_index()
