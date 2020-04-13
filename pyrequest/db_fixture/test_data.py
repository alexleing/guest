import sys, time
sys.path.append('../db_fixture')
# 使用 from mysql_db import DB会有出错
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB


# # 定义过去时间
# past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-100000))
#
# # 定义将来时间
# future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+10000))

# 构造数据
datas = {
    # 发布会数据
    'sign_event': [
        {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心', 'start_time': '2019-01-25 21:42:38', 'create_time': '2019-01-24 15:09:18'},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 200, 'status': 1,
         'address': '北京会展中心', 'start_time': '2019-01-25 21:42:38', 'create_time': '2019-01-24 15:09:18'},
        {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0,
         'address': '北京会展中心', 'start_time': '2019-01-25 21:42:38', 'create_time': '2019-01-24 15:09:18'},
        {'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1,
         'address': '北京会展中心', 'start_time': '2019-01-25 21:42:38', 'create_time': '2019-01-24 15:09:18'},
        {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1,
         'address': '北京国家会议中心', 'start_time': '2019-01-25 21:42:38', 'create_time': '2019-01-24 15:09:18'},
    ],
    # 嘉宾表数据
    'sign_guest': [
        {'id': 1, 'real_name': 'alex', 'phone': 13511001100, 'email': 'alen@mail.com',
         'sign': 0, 'create_time': '2019-01-25 21:42:38', 'event_id':1},
        {'id': 2, 'real_name': '乐春霞', 'phone': 13511001101, 'email': 'alexle@mail.com',
         'sign': 1, 'create_time':'2019-01-25 21:42:38', 'event_id': 1},
        {'id': 3, 'real_name': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com',
         'sign': 0, 'create_time': '2019-01-25 21:42:38', 'event_id': 5},
    ],

}


# 将测试数据插入表内
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()
