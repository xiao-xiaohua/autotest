import unittest
from libs.tools import VerifyClass
from PO.MyP2P.AddBankCard import AddCard

class VerifyBankCard(VerifyClass):
    def setUp(self):
        self.p = AddCard()


    def test_verifycard(self):
        result = self.p.apiAddCard('zxh007','3','1','6','77','709','建设银行五和支行','6223 0066 2346 6664','6223 0066 2346 6664')
        self.verify_code(result,200)
        self.verify_json(result,{"status":1,"info":"\u4fdd\u5b58\u6210\u529f","jump":""})



if __name__ == '__main__':
    unittest.main()