# 03 密码生成器

## 目标

生成指定长度和复杂度的随机密码

## 功能需求

- 让用户输入密码长度
- 让用户选择是否包含大写字母、数字、特殊符号
- 生成并显示密码
- 询问是否重新生成

## 伪代码

在这里写你的伪代码：

```
你的伪代码：
print("欢迎使用密码生成器！")
length = input("请输入密码长度：")
include_uppercase = input("是否包含大写字母？(y/n)：")
include_numbers = input("是否包含数字？(y/n)：")
include_symbols = input("是否包含特殊符号？(y/n)：")
password = generate_password(length, include_uppercase, include_numbers, include_symbols)
def generate_password(length, include_uppercase, include_numbers, include_symbols):
    # 根据用户选择构建字符集
    characters = "abcdefghijklmnopqrstuvwxyz"
    if include_uppercase == "y":
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_numbers == "y":
        characters += "0123456789"
    if include_symbols == "y":
        characters += "!@#$%^&*()"
    
    # 生成随机密码
    password = ""
    for i in range(int(length)):
        password += random.choice(characters)
    
    return password
print("生成的密码是：", password, "，请妥善保管！")
