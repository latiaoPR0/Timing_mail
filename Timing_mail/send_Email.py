import smtplib   #导入PyEmail
from email.mime.text import MIMEText


def sendSMSMsg(msg_from,passwd,msg_to,subject,content):
    msg=MIMEText(content)
    msg["Subject"]=subject
    msg["From"]=msg_from
    msg["To"]=msg_to
     
    try:
        #s = smtplib.SMTP_SSL("smtp.163.com",465)
        s = smtplib.SMTP("smtp.163.com",25)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print ("发送成功")
    except smtplib.SMTPException as e:
        print ("发送失败")
    finally:
        s.quit()