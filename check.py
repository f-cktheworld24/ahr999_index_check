import requests
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_email(ahr999_index):
    # 邮件设置
    mail_content = "太好啦，ahr999_index小于1.2，速速定投！！！当前ahr999_index的值为: {}".format(ahr999_index)
    # sender_address = os.environ['SENDER_EMAIL']
    # sender_pass = os.environ['SENDER_PASSWORD']
    # receiver_address = os.environ['RECEIVER_EMAIL']
    # sender_address = os.getenv('SENDER_EMAIL')
    # sender_pass = os.getenv('SENDER_PASSWORD')
    # receiver_address = os.getenv('RECEIVER_EMAIL')

    # #Setup the MIME
    # message = MIMEMultipart()
    # message['From'] = sender_address
    # message['To'] = receiver_address
    # message['Subject'] = 'AHR999 Index Alert'   #The subject line
    # message.attach(MIMEText(mail_content, 'plain'))

    # #Use QQ's smtp server to send email.
    # session = smtplib.SMTP_SSL('smtp.126.com', 25) #use QQ with port
    # session.login(sender_address, sender_pass) #login with mail_id and password
    # text = message.as_string()
    # session.sendmail(sender_address, receiver_address, text)
    # session.quit()
    
    # 邮件服务器地址和端口号
    smtp_server = 'smtp.163.com'
    smtp_port = 465
    
    # 发件人邮箱地址和密码，以123456@163.com和授权码abcdefg为例子
    sender_email = '123456@163.com'  # 把123456@163.com替换为您自己的发件人邮箱地址
    sender_password = 'abcdefg'  # 这里是你的授权码, 非邮箱登录密码，把abcdefg替换为自己的授权码
    
    # 收件人邮箱地址,以789101112@qq.com为例子
    recipient_email = '789101112@qq.com'
    
    # 创建一封邮件，文本内容为 "太好啦，ahr999_index小于1.2，速速定投！！！当前ahr999_index的值为:xxxx"
    message = MIMEText("太好啦，ahr999_index小于1.2，速速定投！！！当前ahr999_index的值为: {}".format(ahr999_index))
    message['From'] = Header('123456@163.com')  # 设置发件人昵称,把123456@163.com替换为您自己的发件人邮箱地址
    message['To'] = Header('789101112@qq.com')  # 设置收件人昵称,把789101112@qq.com替换为您自己的发件人邮箱地址
    message['Subject'] = Header('AHR999 Index Alert', 'utf-8')  # 设置邮件主题
    
    try:
        # 连接邮件服务器并登录
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(sender_email, sender_password)
    
        # 发送邮件
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())
    
        # 关闭连接
        smtp_connection.quit()
    
        print("邮件发送成功！")
    
    except Exception as e:
        print("邮件发送失败：", e)


def check_ahr999_index():
    response = requests.get('http://43.129.241.254:5000/info/')
    ahr999_index = float(response.json()['ahr999'])
    if ahr999_index < 1.2:
        send_email(ahr999_index)  # Pass ahr999_index as an argument to send_email

if __name__ == "__main__":
    check_ahr999_index()
