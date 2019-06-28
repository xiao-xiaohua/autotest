from libs.tools import BaseHttp


def login():
    #实例化BaseHttp
    run = BaseHttp()
    #将接口url拆分成了host和url，host封装在tools里
    url = '/index.php?ctl=user&act=dologin'
    #登录传参
    login_data = {'email':'zxh007',
            'user_pwd':'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
            'ajax':'1'
    }
    #直接调用tools里的post方法
    result =run.post_data(url=url,data=login_data)
    #用装饰器@classmethod实例化，不需要实例化，可直接通过类名来调用
    # result = BaseHttp.post_data(url=url,data=login_data)
    # 返回多个参数时，用逗号隔开
    #分别返回状态码，响应体
    return result.status_code,result.json()


if __name__ == '__main__':
    #将多个返回值赋予a，会返回元组
    a = login()
    print(a)