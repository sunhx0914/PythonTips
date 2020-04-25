from pymysql import connect


class JD(object):

    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost',port=3306,user='root',password='root',database='jing_dong',charset='utf8')
        # 获得Cursor对象
        self.cs1 = self.conn.cursor()
    
    def __del__(self):
        # 关闭Cursor对象
        self.cs1.close()
        self.conn.close()

    def sql_execute(self,sql):
        count = self.cs1.execute(sql)
        print("共%s条数据 >>>" % count)
        for item in self.cs1.fetchall():
            print(item)

    def show_all_items(self):
        """显示所有商品"""
        sql = "select * from goods;"
        self.sql_execute(sql)

    def show_cates(self):
        sql = "select * from goods_cates;"
        self.sql_execute(sql)

    def show_brands(self):
        sql = "select * from goods_brands;"
        self.sql_execute(sql)
    
    def add_brands(self):
        brand_name = input("请输入新商品品牌名：")
        sql = "insert into goods_brands (name) values ('%s');" % brand_name
        # sql = """insert into goods_brands name values ("%s")""" % brand_name
        self.cs1.execute(sql)
        self.conn.commit()  # 增删改 需要提交
    
    def get_info_by_name(self):
        find_name = input("请输入查询商品的名字：")
        # 非安全的方式
        # 输入 ' or 1=1 or '   (单引号也要输入)
        # sql = "select * from goods where name = '%s';" % find_name
        # print("""--->%s<---""" % sql)
        # --->select * from goods where name = '' or 1=1 or '';<---
        # self.sql_execute(sql)

        # 安全的方式
        # 构造参数列表
        params = [find_name]
        # 执行select语句，并返回受影响的行数：查询所有数据
        sql = "select * from goods where name=%s"
        self.cs1.execute(sql, params)
        # 注意：如果要是有多个参数，需要进行参数化
        # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可
        print(self.cs1.fetchall())

        # sql语句的参数化，可以有效防止sql注入
        # 注意：此处不同于python的字符串格式化，全部使用%s占位
        

    @staticmethod
    def print_menu():
        print("\n------ 京东商城 ------")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        print("4: 添加一个商品品牌")
        print("5: 根据名字查询商品")
        print("0: 退出")
        op = input("请输入功能对应序号：")
        print()
        # return input("请输入功能对应序号：")
        return op

    def run(self):
        while True:
            op = self.print_menu()
            if op == "1":
                self.show_all_items()
            elif op == "2":
                self.show_cates()
            elif op == "3":
                self.show_brands()
            elif op == "4":
                self.add_brands()
            elif op == "5":
                self.get_info_by_name()
            elif op == "0":
                break
            else:
                print("输入有误，请重新输入...")
            

def main():
    # 创建一个京东商城对象
    jd = JD()
    # 调用对象的run方法
    jd.run()


if __name__ == "__main__":
    main()