import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="guest", port=3306)
# 使用cursor方法获取操作游标
cur = db.cursor()
# 查询操作
# 编写SQL查询语句 user对应表名
sql = "select * from sign_guest"
try:
        cur.execute(sql)

        results = cur.fetchall()
        print("id", "real_name", "phone", "email")
        for raw in results:
            id = raw[0]
            real_name = raw[1]
            phone = raw[2]
            email = raw[3]
            print(id, real_name, phone, email)
except Exception as e:
    raise e
finally:
    db.close()

