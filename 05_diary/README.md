# 05 日记本

## 目标

可以按日期写日记并保存

## 功能需求

- 新建日记（自动记录当前日期）
- 查看历史日记列表
- 查看指定日期的日记
- 日记保存在文件中

## 伪代码

在这里写你的伪代码：

```
你的伪代码：
    类似于待办清单，首先包装一个日记类，包含实时日期时间和内容属性
    attribute: date, content
    日期要能实时获取
    date = 获取当前日期时间
    content = 用户输入的日记内容
    日记会保存在特定的文件夹中，文件名以日期命名
    文件路径 = "diary/" + date + ".txt"
    日记本命令行操作
    print("欢迎使用日记本！")
    print("请选择操作：1. 新建日记 2. 查看历史日记 3. 查看指定日期的日记 4. 退出")
    不同操作对应不同方法
    def new_dairy():
        获取当前日期时间
        date = 获取当前日期时间
        获取用户输入的日记内容
        content = input("请输入新日记的内容：")
        保存日记到文件
        文件路径 = "diary/" + date + ".txt"
        with open(文件路径, 'w') as file:
            file.write(content)
        print("日记已保存！")
    def view_history():
        列出diary文件夹中的所有日记文件,并带一个编号
        files = os.listdir("diary/")
        print("历史日记列表：")
        for index, file in enumerate(files, start=1):
            print(f"{index}. {file}")
        用户可能需要查看某一篇日记
        print("请输入要查看的日记的编号：")
        choice = int(input())
        此时自动获取对应文件的路径并查看指定日期的日记
    def view_specific_date(int choice):
        允许传入一个参数，判断是否是从历史记录里访问来的，如果是则直接获取对应文件的路径并查看指定日期的日记
        if choice:
            files = os.listdir("diary/")
            file_path = "diary/" + files[choice - 1]
            with open(file_path, 'r') as file:
                content = file.read()
            print(f"日记内容：{content}")
        否则则让用户输入一个日期，获取对应文件的路径并查看指定日期的日记
        else:
            date = input("请输入要查看的日记的日期（格式：YYYY-MM-DD）：")
            file_path = "diary/" + date + ".txt"
            此时做一个判断，如果文件存在则打开查看，否则提示没有找到该日期的日记
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                print(f"日记内容：{content}")
            else:
                print("没有找到该日期的日记！")
    整体会通过一个循环来实现命令行操作，直到用户选择退出
    while True:
        choose = input("请选择操作：1. 新建日记 2. 查看历史日记 3. 查看指定日期的日记 4. 退出")
        if choose == '1':
            new_dairy()
        elif choose == '2':
            view_history()
        elif choose == '3':
            view_specific_date(0)
        elif choose == '4':
            print("感谢使用日记本，再见！")
            break
        else:
            print("无效的选择，请重新输入！")
