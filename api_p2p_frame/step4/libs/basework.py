from libs.tools import BaseHttp


def apiLogin():
    #实例化BaseHttp
    run = BaseHttp()
    #将接口url拆分成了host和url，host封装在tools里
    url = '/index.php?ctl=user&act=dologin'
    #登录传参
    login_data = {'email':'zxh007',
            'user_pwd':'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
            'ajax':'1'
    }
    result = run.http_send(url=url,data=login_data)
    # 方式一:
    headers = result.headers['Set-Cookie']
    pid = headers.split('=')[1].split(';')[0]
    #方式二：
    # pid = result.cookies['PHPSESSID']
    return pid



if __name__ == '__main__':

   pid=apiLogin()
   print(pid)