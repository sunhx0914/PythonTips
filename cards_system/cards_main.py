import cards_tools

cards_list = []
exit_flag = True

while exit_flag:
    cards_tools.show_meau()
    while True:     # 这个while可改为 list判断
        choose = input("请输入选项：")
        if cards_tools.input_num(choose):
            break
        else:
            print("输入不合法，请重新输入！")
    exit_flag = cards_tools.meau_choose(int(choose), cards_list)


"""
# 无限循环，由用户主动决定什么时候退出循环！
while True:
    # 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        # in 避免 or 拼接
        # 没使用int转换 可避免出错
        if action_str == "1":   # 新增名片
            cards_tools.new_card()
        elif action_str == "2":     # 显示全部
            cards_tools.show_all()
        elif action_str == "3":     # 查询名片
            cards_tools.search_card()
    elif action_str == "0":     # 0 退出系统
        print("欢迎再次使用【名片管理系统】")
        break
        # 不希望立刻编写分支内部的代码，可以使用 pass 关键字，表示一个占位符
    else:   # 其他内容输入错误，需要提示用户
        print("您输入的不正确，请重新选择")
"""