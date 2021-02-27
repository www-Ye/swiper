# -*- codeing = utf-8 -*-
# @Time : 2021/2/27 21:19
# @Author : wy
# @File : config.py
# @Software : PyCharm

'''
第三方配置
'''

# 互亿无线短信配置
HY_SMS_URL = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C13743706',
    'password': 'e9cc641d4590d9bff40c596bd9626980',
    'content': '您的验证码是：%s。请不要把验证码给别人。',
    'mobile': None,
    'format': 'json'
}