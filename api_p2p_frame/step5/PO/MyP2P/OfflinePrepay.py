from libs.basework import LoginClass


class OfflinePrepayClass(LoginClass):
    def apiOfflinePrepay(self,money,memo,check_ol_bl_pay='on',payment='5',bank_id='0'):
        prepay_url = '/member.php?ctl=uc_money&act=incharge_done'
        prepay_data = {'check_ol_bl_pay':check_ol_bl_pay,
                       'money':money,
                       'pingzheng':'',
                       'memo':memo,
                       'payment':payment,
                       'bank_id':bank_id
        }
        # self.apiLogin('zxh007',
        #              'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
                     # '1')

        self.http_send(url=prepay_url,data=prepay_data,cookies=self.cookies)
        #检查是否充值成功
        check_url = '/member.php?ctl=uc_money&act=incharge_log'
        result = self.http_send(method='get',url=check_url,cookies=self.cookies)
        #如果有多个返回值，最好用元组的形式，因为元组是不可修改的，安全性更高
        return result


if __name__ == '__main__':
    run = OfflinePrepayClass()
    run.apiLogin('xhz622',
                 'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
                 '1')
    result = run.apiOfflinePrepay('153','22222325')
