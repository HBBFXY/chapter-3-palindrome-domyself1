# 回文数判断程序
n = input("请输入一个5位数字：")
# 判断输入是否为纯数字，且长度是否为5
if not n.isdigit() or len(n) != 5:
    print("输入错误：必须输入一个5位数字！")
else:
    # 判断是否为回文数
    if n == n[::-1]:  
        print("是回文数")
    else:
        print("不是回文数")
