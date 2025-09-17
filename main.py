num = input("")
if not num.isdigit() or len(num) != 5:
    print("输入错误：必须输入一个5位数字！")
else:
    if num == num[::-1]: 
        print("是回文数")
    else:
        print("不是回文数")

