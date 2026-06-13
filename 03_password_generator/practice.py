import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase

    # 根据用户选择添加字符类型
    if include_uppercase == "y":
        characters += string.ascii_uppercase
    if include_numbers == "y":
        characters += string.digits
    if include_symbols == "y":
        characters += "!@#$%^&*()"

    password = ""
    for i in range(length):
        # 最终的密码会在整个字符串中随机选择字符
        password += random.choice(characters)

    return password

def main():
    print("欢迎使用密码生成器！")

    length = int(input("请输入密码长度："))
    include_uppercase = input("是否要包含大写字母？(y/n)：")
    include_numbers = input("是否要包含数字？(y/n)：")
    include_symbols = input("是否要包含特殊符号？(y/n)：")

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    print(f"生成的密码是：{password}，请妥善保管！")

    play_again = input("是否重新生成？(y/n)：")
    if play_again == "y":
        main()

if __name__ == "__main__":
    main()
