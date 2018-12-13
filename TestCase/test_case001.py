import requests
import unittest

class Interface(unittest.TestCase):
    def setUp(self):
 #       self.ip = 'http://172.16.10.34'
 #       self.port = '9091'
 #       self.adrPath = 'dsIntegration-manager/api/biz/service/testService'
 #       self.param =
        self.headers = {'Cookie':'JSESSIONID=ef5bf288-eeb3-4275-979f-145ef4002010'}
        self.url = 'http://172.16.10.34:9091/dsIntegration-manager/api/biz/service/testService?tokenKey=36103b0a-07ac-4777-abb1-d6d10e11c096&modelId=1134078&serviceCode=20181122'
        pass
    def tearDown(self):
        pass


    def test_get(self):
        response = requests.get(url=self.url,headers=self.headers)

        if 200 == response.status_code:
            print('success')
        else:
            print('fail')

    def test_post(self):
        reponse = requests.post()


if __name__ == '__main__':
    unittest.main()