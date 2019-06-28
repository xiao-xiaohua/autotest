from libs.basework import LoginClass


class AddCard(LoginClass):
    def apiAddCard(self,real_name,bank_id,region_lv1,region_lv2,region_lv3,region_lv4,bankzone,bankcard,reBankcard):
        #添加银行卡
        bank_url = '/member.php?ctl=uc_money&act=savebank'
        card_data = {'real_name':real_name,
                     'bank_id':bank_id,
                     'otherbank':'',
                     'region_lv1':region_lv1,
                     'region_lv2':region_lv2,
                     'region_lv3':region_lv3,
                     'region_lv4':region_lv4,
                     'bankzone':bankzone,
                     'bankcard':bankcard,
                     'reBankcard':reBankcard
        }

        #登录请求
        self.apiLogin('zxh007',
                     'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
                     '1')
        result = self.http_send(url=bank_url,data=card_data,cookies = self.cookies)
        # #获取cookies
        # pid = result.cookies['PHPSESSID']
        # cookies = {
        #   'PHPSESSID':pid
        # }
        return result



if __name__ == '__main__':
    run = AddCard()
    result = run.apiAddCard('zxh007','3','1','6','77','709','建设银行五和支行','6223 0066 2346 6664 1234 5','6223 0066 2346 6664 1234 5')

