import unittest
import requests




class appNewProductDetailTest(unittest.TestCase):
    '''调用新品详情接口'''


    def setUp(self):
        self.base_url = "https://app-uat.maxxipoint.com/api/newProduct/detail"

    def tearDown(self):
        print(self.result)

    def test_app_new_product_detail(self):
        '''新品详情接口'''
        payload = "{\"bizContent\":\"{'memberId':'1421381708','contentId':'9635','supportType':'1'}\"," \
                  "\"devContent\":\"{'appIdentify':'com.maxxipoint.iosTest','" \
                  "deviceId':'35ad6e2bb310c564b0eff4715d07f83adbedb33d','deviceModel':'iPhone 8'," \
                  "'appVersion':'5.5.0','deviceVersion':'12.1.2','platform':'iOS'}\"}"
        header = {
            'requestid': "2122",
            'appid': "APPKHFJJ78897FH",
            'timestamp': "20190129090320",
            'reqtype': "app",
            'tokenid': "3F1C2083CD8FD7F6CF5D6062C9E6871723EAB325",
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "72919a71-eace-30a0-e163-f743965ff2a2"
        }

        r = requests.post(self.base_url, headers=header, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], '200')
        self.assertEqual(self.result['message'], '成功')
