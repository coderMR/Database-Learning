
# -*- coding=utf-8 -*-

import pymysql

class JDMySQLHelper(object):

    def __init__(self, host, port, db, user, password, charset):
        self.conn = pymysql.connect(host = host, port = port, db = db, user = user, password = password, charset = charset )
        self.cursor = self.conn.cursor()
        self.is_login = False

    def run(self):
        while True:
            op_code = self.show_menu()
            if op_code == 1:
                self.show_goods()
            elif op_code == 2:
                self.show_brands()
            elif op_code == 3:
                self.show_cates()
            elif op_code == 4:
                self.add_brand()
            elif op_code == 5:
                self.regist()
            elif op_code == 6:
                self.login()
            elif op_code == 7:
                self.add_order()
            elif op_code == 8:
                print('退出')
                break

    @staticmethod
    def show_menu():
        print('1.展示所有商品信息')
        print('2.展示所有品牌信息')
        print('3.展示所有类别信息')
        print('4.添加品牌')
        print('5.注册')
        print('6.登录')
        print('7.下订单')
        print('8.退出')
        return int(input('请选择要执行的操作:'))

    def show_goods(self):
        sql = "SELECT * FROM Goods;"
        self.execute(sql, None)

    def show_brands(self):
        sql = "SELECT * FROM Good_brand_names"
        self.execute(sql, None)

    def show_cates(self):
        sql = "SELECT * FROM Good_cate_names"
        self.execute(sql, None)

    def add_brand(self):
        brand = input('请输入一个品牌:')
        sql = "INSERT INTO Good_brand_names VALUES (DEFAULT, %s)"
        self.execute(sql, [brand]) 
    def regist(self):
        # 获取用户信息
        name = input('请输入用户名:')
        address = input('请输入地址:')
        phone = input('请输入手机号:')
        password = input('请输入密码:')

        # 唯一性校验
        sql = "SELECT name, phone FROM Users WHERE name = %s or phone = %s"
        records = self.execute(sql, [name, phone])
        if len(records):
            print('用户名或手机号已存在')
            return
        
        # 插入用户
        sql = "INSERT INTO Users VALUES (DEFAULT, %s, %s, %s, %s)"
        self.execute(sql, [name, address, phone, password])

    def login(self):
        # 获取用户信息
        account = input('请输入用户名或手机号:')
        password = input('请输入密码:')
        
        # 校验
        sql = "SELECT * FROM Users WHERE (%s = name or %s = phone) AND %s = password"
        records = self.execute(sql, [account, account, password])
        if len(records):
            self.is_login = True
            print('登录成功')
        else:
            print('用户名或密码错误')

    def add_order():
        if self.is_login == False:
            print('没有权限,请先登录')
            return



    def execute(self, sql, params):
        self.cursor.execute(sql, params) # 这样可以避免sql注入攻击
        self.conn.commit()
        records = self.cursor.fetchall()
        if len(records):
            print('-' * 10)
            for record in records:
                print(record)
            print('-' * 10)
        return records

    def __del__(self):
        self.cursor.close()
        self.conn.close()

def main():
    helper = JDMySQLHelper(host = 'localhost', port = 3306, db = 'Persons', user = 'root', password = 'zch196511', charset = 'utf8')
    helper.run()

if __name__ == '__main__':
    main()
