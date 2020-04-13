import unittest
import requests
import os, sys
import time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
# try:
#     from db_fixture import test_data
# except ImportError:
#     from .db_fixture import test_data
# 定义过去时间
# past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-100000))
#
# # 定义将来时间
# future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+10000))


class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid':'','name':'','limit':'','status': '','address':'','start_time':'', 'create_time': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid': 1, 'name': '红米Pro发布会1', 'limit': 2000, 'status': 1,'address': '北京会展中心',
                   'start_time': '2019-01-25 21:42:38', 'create_time': '2019-01-24 15:09:18'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 100022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid':11,'name':'红米Pro发布会','limit':2000,'status': 1,'address':'深圳宝体',
                   'start_time':'2019-01-25 21:42:38','create_time':'2019-01-24 15:09:18'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['statue'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid':11,'name':'一加4手机发布会2','limit':2000,'address':"深圳宝体",
                   'start_time':'测试时间','create_time':'测试时间'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 100024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid':10,'name':'一加4手机发布会1','limit':2000,'address':"深圳宝体",
                   'start_time':'2019-01-25 21:42:38','create_time':'2019-01-24 15:09:18'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


# if __name__ == '__main__':
#     test_data.init_data() # 初始化接口测试数据
# unittest.main()
