import requests


#抓包得到的接口地址
# login_url = 'http://localhost/index.php?ctl=user&act=dologin&fhash=uLWNLwmuPEOyqrxGpYTeojxcFXAmyXSPXvVVvPRaHVEjNlohzt'
#&fhash后传参的作用：新增字段时可不用再定义字段，
# 做接口测试时，可将&fhash部分去掉
login_url = 'http://localhost/index.php?ctl=user&act=dologin'

login_data = {'email':'zxh007',
        'user_pwd':'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
        'ajax':'1'
}


result = requests.post(url=login_url,data=login_data)
code = result.status_code
state = result.json()
print(code)
print(state)


#校验是否登录成功
if code == 200 and state['info'] == '成功登录':
    print('测试通过')
