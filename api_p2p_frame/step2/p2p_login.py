import requests

def login():
    #登录接口url
    login_url = 'http://localhost/index.php?ctl=user&act=dologin'
    #登录传参
    login_data = {'email':'zxh007',
            'user_pwd':'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
            'ajax':'1'
    }
    result = requests.post(url=login_url,data=login_data)
    # 返回响应体
    return result.status_code,result.json()



code,state =login()
print(code,state)