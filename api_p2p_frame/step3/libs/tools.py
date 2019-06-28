import requests


class BaseHttp(object):
    host = 'http://localhost'
    
    @classmethod
    def post_data(self,url,data,icon=1,*args,**kwargs):
        '''
        
        :param url: 拆分后的url部分
        :param data: post传参
        :param icon: 
        :param args: 
        :param kwargs: 
        :return: 
        '''
        #将host与 url进行拼接，括号里的url是函数里的url
        url = '{}{}'.format(self.host,url)   
        if icon == 1:
            #传的url是拼接后的url
            result = requests.post(url=url,data=data,*args,**kwargs)
        elif icon == 2:
            result = requests.post(url=url, file=data, *args, **kwargs)
        return result
    
    def get_data(self,url,data,icon=1,*args,**kwargs):
        '''
        :param url: 拆分后的url部分
        :param data: get传参
        :param icon: 
        :param args: 
        :param kwargs: 
        :return: 
        '''
        url = '{}{}'.format(self.host,url)
        if icon == 1:
            result = requests.get(url=url,params=data,*args,*kwargs)
        return result
        
    