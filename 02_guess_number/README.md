# 02 猜数字游戏

## 目标

电脑随机生成一个数字，用户猜测，直到猜中

## 功能需求

- 随机生成1-100之间的整数
- 用户输入猜测的数字
- 提示"大了"或"小了"
- 猜中后显示猜测次数
- 询问是否再玩一次

## 伪代码

在这里写你的伪代码：

```
你的伪代码：
import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("1-100之间猜个数: "))
        猜测次数count += 1
        if guess < number:
            print("太小了！")
        elif guess > number:
            print("太大了！")
        else:
            print(f"恭喜你！你在 {猜测次数count} 次尝试中猜中了数字。")
            print("你想再玩一次吗？ (yes/no)")
            play_again = input().lower()
            if play_again == 'yes':
                guess_number()
            break