import unittest
from libs.tools import VerifyClass
from PO.MyP2P.OfflinePrepay import OfflinePrepayClass



class VerifyPrepay(VerifyClass):
    def setUp(self):
        self.p = OfflinePrepayClass()


    def test_verifyprepay(self):
        self.p.apiLogin('zxh007',
                     'ZWdZZmlQQ21kT0FQck9MZWlsU2htSFhnVWlmUnhBTkRkd0N6emdSWFV0VkpnV1VhdnklMjV1NjVCOSUyNXU3RUY0enhoMTIzNDU2JTI1dThGNkYlMjV1NEVGNg==',
                     '1')
        result = self.p.apiOfflinePrepay('222','22222267')
        self.verify_code(result,200)
        self.verify_html(result,'22222267')



if __name__ == '__main__':
    unittest.main()