from libs.tools import BaseHttp
from libs.basework import apiLogin



def apiOfflinePrepay():
    prepay_url = '/member.php?ctl=uc_money&act=incharge_done'
    prepay_data = {'check_ol_bl_pay':'on',
                   'money':'200',
                   'pingzheng':'',
                   'memo':'22222224',
                   'payment':'5',
                   'bank_id':'0'
    }
    #获取cookies
    pid = apiLogin()
    cookies = {'PHPSESSID':pid}
    #实例化BaseHttp
    run = BaseHttp()
    run.http_send(url=prepay_url,data=prepay_data,cookies=cookies)
    #检查是否充值成功
    check_url = '/member.php?ctl=uc_money&act=incharge_log'
    result = run.http_send(method='get',url=check_url,cookies=cookies)
    return result.text


if __name__ == '__main__':
   result = apiOfflinePrepay()
   print(result)

