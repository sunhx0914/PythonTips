
def show_meau():
    """
    打印菜单
    """
    print()
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0", end="\n\n")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片", end="\n\n")
    print("0. 退出系统")
    print("*" * 50, end="\n\n")


def input_num(num):
    """
    输入判断
    """
    if num.isdecimal() and (int(num) in range(4)) :
        return True
    else:
        return False


def query_input_num(num):
    """
    输入判断
    """
    if num.isdecimal() and (int(num) in range(1,4)) :
        return int(num)
    else:
        return False


def create_crad():
    """
    新建名片
    """
    dict_card = {}
    print("-" * 50)
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入Email：")
    print("-" * 50)
    dict_card["name"] = name
    dict_card["tel"] = tel
    dict_card["qq"] = qq
    dict_card["email"] = email
    return dict_card


def show_all(card_list):
    """
    显示全部
    """
    if not card_list:
        print("-" * 50)
        print("暂无名片！")
        print("-" * 50)
    for item in card_list:
        print("-" * 50)
        print("姓名: %s" % item["name"])
        print("电话: %s" % item["tel"])
        print("QQ: %s" % item["qq"])
        print("Email: %s" % item["email"])
        # for key,value in item.items():
        #     print("%s：%s" % (item[key], item[value]))
        print("-" * 50)


def edit_input(concent, card_list, query_index, key):
    """
    判断是否修改
    """
    if len(concent) > 0:
        card_list[query_index][key] = concent


def edit_card(card_list, query_index):
    """
    修改名片
    """
    print("-" * 50)
    name = input("请输入姓名(不修改回车)：")
    tel = input("请输入电话(不修改回车)：")
    qq = input("请输入QQ(不修改回车)：")
    email = input("请输入Email(不修改回车)：")
    print("-" * 50)
    edit_input(name, card_list, query_index, "name")
    edit_input(tel, card_list, query_index, "tel")
    edit_input(qq, card_list, query_index, "qq")
    edit_input(email, card_list, query_index, "email")
    


def query_meau(card_list, query_index):
    while True:
        edit_choose = input("请输入选项(1.删除/2.修改/3.返回)：")
        if query_input_num(edit_choose) == 1:
            card_list.pop(query_index)
            print("成功删除名片！")
            break
        elif query_input_num(edit_choose) == 2:
            edit_card(card_list, query_index)
            print("修改成功！")
            break
        elif query_input_num(edit_choose) == 3:
            break
        else:
            print("输入不合法，请重新输入！")


def query_card(card_list):
    """
    查询名片
    """
    while True:
        query_index = -1
        print("-" * 50)
        query_name = input("请输入查询姓名：")
        for item in card_list:
            if query_name in item.values():
                query_index = card_list.index(item)
                break
        print("-" * 50)
        if query_index < 0:
            print("无数据！")
        else:
            print("查询结果：query_index " + str(query_index))
            print(card_list[query_index].keys())
            # for item in card_list[query_index].keys():
            print("姓名: %s" % card_list[query_index]["name"])
            print("电话: %s" % card_list[query_index]["tel"])
            print("QQ: %s" % card_list[query_index]["qq"])
            print("Email: %s" % card_list[query_index]["email"])
            query_meau(card_list, query_index)
            break


def meau_choose(num, card_list):
    if num == 1:
        new_card = create_crad()
        card_list.append(new_card)
        print("--- ", card_list)
    elif num == 2:
        show_all(card_list)
    elif num == 3:
        query_card(card_list)
    else:
        print("即将退出...")
        return False
    return True
        # return pass