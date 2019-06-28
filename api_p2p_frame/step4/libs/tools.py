import requests


class BaseHttp(object):
    #定义类变量
    host = 'http://localhost'

    def http_send(self,url,method='post',*args,**kwargs):
        url = '{}{}'.format(self.host, url)
        # print('url is',url)
        # print('method is',method)
        result = requests.request(method=method,url=url,*args,**kwargs)
        return result

