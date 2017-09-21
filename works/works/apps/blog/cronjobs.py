#coding=utf-8

import datetime
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings


def send_reminder_mail():
    date = timezone.localtime(timezone.now()).strftime("%Y年%m月%d日 %H:%M:%S")
    subject = "读书，撸代码，学算法————提醒！"
    message = """
    <body class='typora-export' >
    <div>{}</div>
    <div  id='write'  class = 'is-mac'><h2><a name='header-n0' class='md-header-anchor '></a>坚持的力量</h2><h3><a name='header-n5' class='md-header-anchor '></a>行路难（其一）</h3><h5><a name='header-n83' class='md-header-anchor '></a>【作者】李白 · 唐</h5><h5><a name='header-n17' class='md-header-anchor '></a>金樽清酒斗十千，玉盘珍羞直万钱。</h5><h5><a name='header-n19' class='md-header-anchor '></a>停杯投箸不能食，拔剑四顾心茫然。</h5><h5><a name='header-n21' class='md-header-anchor '></a>欲渡黄河冰塞川，将登太行雪满山。</h5><h5><a name='header-n23' class='md-header-anchor '></a>闲来垂钓碧溪上，忽复乘舟梦日边。</h5><h5><a name='header-n25' class='md-header-anchor '></a>行路难！行路难！多歧路，今安在？</h5><h5><a name='header-n27' class='md-header-anchor '></a>长风破浪会有时，直挂云帆济沧海。</h5><p></p><h3><a name='header-n58' class='md-header-anchor '></a>登鹳雀楼_百度汉语</h3><h5><a name='header-n61' class='md-header-anchor '></a>【作者】：王之涣</h5><h5><a name='header-n63' class='md-header-anchor '></a>白日依山尽，黄河入海流。</h5><h5><a name='header-n71' class='md-header-anchor '></a>欲穷千里目，更上一层楼。</h5><p></p><p>读书时长，工作收获，算法笔记！</p><p>注释：此消息需要更新成链接，可以填写 input 的页面。填完后自动保存到数据库</p><p></p></div>
    </body>
    """.format(date)
    recipient = ['838450207@qq.com']
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient, html_message=message)