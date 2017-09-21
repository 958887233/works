#coding=utf-8

import datetime
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings


def send_reminder_mail():
    date = timezone.now().strftime("%Y年%m月%d日 %H:%M:%S")
    subject = "读书，撸代码，学算法————提醒！"
    message = """{}读书时长，工作收获，算法笔记！
                注释：此消息需要更新成链接，可以填写 input 的页面。填完后自动保存到数据库。

    """.format(date)
    recipient = ['838450207@qq.com']
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient)