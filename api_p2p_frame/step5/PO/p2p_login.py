from libs.tools import BaseHttp


#继承BaseHttp
class LoginClass(BaseHttp):
    cookies = {'PHPSESSID':''}
    def apiLogin(self,email,user_pwd,ajax):
        #将接口url拆分成了host和url，host封装在tools里
        url = '/index.php?ctl=user&act=dologin'
        #登录传参
        login_data = {'email': email,
                      'user_pwd': user_pwd,
                      'ajax': ajax
                      }
        result = self.http_send(url=url,data=login_data)
        # 方式一:
        headers = result.headers['Set-Cookie']
        pid = headers.split('=')[1].split(';')[0]
        self.cookies['PHPSESSID'] = pid
        #方式二：
        # pid = result.cookies['PHPSESSID']
        # self.cookies['PHPSESSID'] = pid
        return result



if __name__ == '__main__':
    run = LoginClass()
    run.apiLogin('zxh007',
                 'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
                 '1')
    print(run.cookies)

