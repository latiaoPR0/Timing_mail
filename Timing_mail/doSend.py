# -*- coding: utf-8 -*-
from getsencel import getSentenceList
from send_Email import sendSMSMsg
import time
import datetime

sentenceList = getSentenceList("http://www.1juzi.com/new/150542.html")

TIME_TO_DO = '16:33:00'  # 发送时间点
now_time = datetime.datetime.now()
MSG_SUFFIX = '\n来自你的小可爱——憨憨'  # 短信后缀
msg_from = "xxxxxx@163.com"    #发件人邮箱
passwd = "xxxxxx"  #客户端授权密码,不是邮箱登陆密码
msg_to = "xxxxxx@qq.com"  #接收人邮箱
subject = str(now_time)+":    这是我想对你说的话(电脑自动发送)" #邮件的标题
#content = "这是一条测试的内容"
SEND_TO_ME = '舔狗，给女神发的短信已经用光了，快来更新！！！'
SEND_TO_ME_subject = '短信已经用光！！！'


def doSend():
    index = 0  # 下一条短信的下标
    
    while True:
        # 刷新
        time_now = time.strftime("%H:%M:%S", time.localtime())
        # 此处设置每天定时的时间
        if time_now == TIME_TO_DO:
            # 需要执行的动作
            # 判断当前list有没有用光
            if index >= len(sentenceList):
                # 用光了就短信通知我
                sendSMSMsg(msg_from,passwd,msg_from,SEND_TO_ME_subject,SEND_TO_ME);
                # 跳出
                break
    
            # 给女神发短信
            content = sentenceList[index] + MSG_SUFFIX
            sendSMSMsg(msg_from,passwd,msg_to,subject,content);
    
            # 下标加一
            index += 1
    
            # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次
            time.sleep(2)

# 主程序入口
if __name__ == '__main__':
    doSend()