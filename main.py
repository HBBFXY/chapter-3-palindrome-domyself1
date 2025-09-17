# 回文数判断程序

num = input("请输入一个5位数字：")

# 判断输入是否为纯数字，且长度是否为5
if not num.isdigit() or len(num) != 5:
    print("输入错误：必须输入一个5位数字！")
else:
    # 判断是否为回文数
    if num == num[::-1]:  # 使用字符串切片反转
        print("是回文数")
    else:
        print("不是回文数")

