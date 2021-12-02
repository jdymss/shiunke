#!/usr/bin/env python
-- coding: UTF-8 --
author  libertyspy
link    http://www.lastme.com
import socket
import smtplib
import urllib
mail_options = {
    'server':'smtp.qq.com',#使用了QQ的SMTP服务，需要在邮箱中设置开启SMTP服务
    'port':25,             #端口
    'user':'hacker@qq.com',#发送人
    'pwd':'hacker',        #发送人的密码
    'send_to':'sniper@qq.com',  #收件者
}
msg_options={
    'user':'hacker',    #短信平台的用户名
    'pwd':'74110',      #短信平台的密码
    'phone':'12345678910',   #需要发短信的电话号码
}
test_host = 'http://www.lastme.com/'
def url_request(host,port=80):
    try:
        response = urllib.urlopen(host)
        response_code = response.getcode()
        if 200 != response_code:
            return response_code
        else:
            return True
    except IOError,e:
        return False
def send_message(msg,host,status):
    send_msg='服务器:%s挂了！状态码：%s' % (host,status)
    request_api="http://www.uoleem.com.cn/api/uoleemApi?username=%s&pwd=%s&mobile=%s&content=%s&quot;  \
            % (msg['user'],msg['pwd'],msg['phone'],send_msg)
    return url_request(request_api)
def send_email(mail,host,status):
    smtp = smtplib.SMTP()
    smtp.connect(mail['server'], mail['port'])
    smtp.login(mail['user'],mail['pwd'])
    msg="From:%s\rTo:%s\rSubject:服务器: %s 挂了 !状态码:%s\r\n" \
         % (mail['user'],mail['send_to'],host,status)
    smtp.sendmail(mail['user'],mail['send_to'], msg)
    smtp.quit()
"""
def check_status(host,port=80):
    s = socket.socket()
    ret_msg = []
    try:
        s.connect((host,port))
        return True
    except socket.error,e:
        return False
"""
if name=='main':
    status = url_request(test_host)
    if status is not True and status is not None:
        send_email(mail_options,test_host,status)
        send_message(msg_options,test_host,status)
    else:
        pass</pre> 