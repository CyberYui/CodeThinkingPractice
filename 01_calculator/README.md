# 01 计算器

## 目标

实现一个命令行计算器，支持加减乘除和平方根

## 功能需求

- 显示菜单让用户选择运算类型
- 根据选择获取用户输入的数字
- 计算并输出结果
- 可以重复计算直到用户选择退出

## 伪代码

在这里写你的伪代码，用中文描述程序流程：

```
1. 显示菜单：1加法 2减法 3乘法 4除法 5平方根 0退出
2. 获取用户选择
3. 如果是0，退出程序
4. 如果是5，获取一个数字，计算平方根，显示结果
5. 如果是1-4，获取两个数字，进行对应运算，显示结果
6. 回到第1步
```

你的伪代码：
import math
cybercalculator.py
print("Welcome to CyberCalculator！")
print("「"&("-" * 30)&"｜")
print("|Please select an operation:")
print("|1. Addition")
print("|2. Subtraction")
print("|3. Multiplication")
print("|4. Division")
print("|5. Square Root")
print("|0. Exit")
print("｜"&("-" * 30)&"」")
operation = input("Enter your choice: ")
switch operation:
    case "0":
        print("Goodbye!")
    case "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result: ", result)
    case "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result: ", result)
    case "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result: ", result)
    case "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            result = num1 / num2
            print("Result: ", result)
        else:
            print("Error: Division by zero")
    case "5":
        num = float(input("Enter a number: "))
        if num >= 0:
            result = math.sqrt(num)
            print("Result: ", result)
        else:
            print("Error: Cannot calculate square root of a negative number")
    default:
        print("Invalid choice, please try again.")
