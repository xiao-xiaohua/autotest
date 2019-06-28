import unittest

from PO.p2p_login import login


class TestLogin(unittest.TestCase):

    def test_login(self):
        code,state = login()
        self.assertEquals(code,200)
        self.assertEquals(state['info'],'成功登录')




if __name__ == '__main__':
    unittest.main()
