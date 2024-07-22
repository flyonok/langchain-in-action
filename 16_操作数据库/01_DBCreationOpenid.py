# 导入sqlite3库，它是Python内置的轻量级数据库。
import sqlite3

# 连接到数据库
conn = sqlite3.connect('FlowerShop.db')
cursor = conn.cursor()

# 执行SQL命令来创建Flowers表
cursor.execute('drop table if exists wxUsers')
cursor.execute('''
        CREATE TABLE wxUsers (
            ID INTEGER PRIMARY KEY, 
            openid TEXT NOT NULL, 
            status TEXT NOT NULL, 
            fileName TEXT NOT NULL, 
            lastprompt TEXT NOT NULL, 
            createtime DATE
        );
    ''')

# 插入5种鲜花的数据
users = [
    ('o99w16VznTCcbwrmSNTkCV0kbqJg', '同意', 'wxtddggg.txt','', '2023-12-31'),
    ('o5zrG0xQ7w16fQ67FoihwwbRXy4E', '不太同意', '哈哈哈.txt','', '2024-01-03'),
    ('o5zrG0yjeA4Ve0HlE3cTbp8S3ink', '同意', '个阿迪的.txt','', '2023-12-31'),
    ('o5zrG03-stqQ4MOlTvOXenEHUp_4', '同意', '挨打的.txt','', '2023-12-31'),
    ('o99w16Tu5x0eyv5_AOXXoilZ6bbI', '同意', '啊发放的.txt','', '2023-12-31'),
]

for user in users:
    cursor.execute('''
        INSERT INTO wxUsers (openid, status, fileName, lastprompt, createtime) 
        VALUES (?, ?, ?, ?, ?);
    ''', user)

# 提交更改
conn.commit()

# 关闭数据库连接
conn.close()
