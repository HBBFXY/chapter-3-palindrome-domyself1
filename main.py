# 获取用户输入
user_input = input("请输入一个5位数字：")
# 严格验证输入是否为5位纯数字
if len(user_input) != 5 or not user_input.isdigit():
    print("输入错误，必须是5位纯数字")
else:
    # 检查是否为回文数（正向与反向一致）
    if user_input == user_input[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
