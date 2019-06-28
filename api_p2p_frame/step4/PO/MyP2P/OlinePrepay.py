from libs.tools import BaseHttp
from libs.basework import apiLogin


def apiOlinePrepay():
    #选择支付宝支付的接口
    alipay_url = 'http://localhost/index.php?ctl=ajax&act=payment_fee'
    #线上支付的接口
    online_url = 'http://localhost/member.php?ctl=uc_money&act=incharge_done'
    #