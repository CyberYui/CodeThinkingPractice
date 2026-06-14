# 04 待办事项管理器

## 目标

命令行版待办事项管理，支持增删改查

## 功能需求

- 添加待办事项
- 查看所有待办
- 标记完成
- 删除待办
- 数据保存在文件中

## 伪代码

在这里写你的伪代码：

你的伪代码：

```python
class TodoItem:
    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = False

def show_tudo_list(todo_list):
    # 显示待办事项列表,借用enumerate函数显示索引
    for index, item in enumerate(todo_list):
        status = "已完成" if item.completed else "未完成"
        print(f"{index}. {item.title} - {item.description} [{status}]")

def load_todo_list(filename):
    # 从文件加载待办事项列表
    file = open(filename, "r")
    todo_list = []
    for line in file:
        title, description, completed = line.strip().split("|")
        item = TodoItem(title, description)
        item.completed = completed
        todo_list.append(item)
    file.close()
    return todo_list

def save_todo_list(todo_list, filename):
    # 将待办事项列表保存到文件
    file = open(filename, "w")
    for item in todo_list:
        line = f"{item.title}|{item.description}|{item.completed}\n"
        file.write(line)
    file.close()

def add_todo_item(todo_item, todo_list):
    # 添加新的待办事项
    todo_list.append(todo_item)

def delete_todo_item(todo_list, index):
    # 删除待办事项
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
    else:
        print("无效的待办事项编号")

def main():
    print("欢迎使用待办事项管理器")
    filename = input("请输入想要使用的文件名：")+".txt"
    if os.path.exists(filename):
        todo_list = load_todo_list(filename)
    else:
        open(filename, "w").close()  # 创建新文件
        todo_list = []
    print("允许操作：1. 添加待办事项 2. 查看所有待办事项 3. 标记完成 4. 删除待办事项 5. 保存文件 6. 退出")
    choice = input("请输入操作编号：")
    int(choice)
    print("-"*30)
    # 借助while循环实现持续操作，直到用户选择退出
    while True:
        if choice == 1:
            title = input("请输入待办事项标题：")
            description = input("请输入待办事项描述：")
            # 默认未完成,所以不需要输入completed
            item = TodoItem(title, description)
            add_todo_item(item, todo_list)
            print("当前待办事项列表：")
            show_tudo_list(todo_list)
            print("-"*30)
        elif choice == 2:
            print("当前待办事项列表：")
            show_tudo_list(todo_list)
            print("-"*30)
        elif choice == 3:
            index = int(input("请输入要标记完成的待办事项编号："))
            if 0 <= index < len(todo_list):
                todo_list[index].completed = True
            print("当前待办事项列表：")
            show_tudo_list(todo_list)
            print("-"*30)
        elif choice == 4:
            index = int(input("请输入要删除的待办事项编号："))
            delete_todo_item(todo_list, index)
            print("当前待办事项列表：")
            show_tudo_list(todo_list)
            print("-"*30)
        elif choice == 5:
            save_todo_list(todo_list, filename)
            print("待办事项已保存")
            print("-"*30)
        elif choice == 6:
            save_todo_list(todo_list, filename)
            print("待办事项已保存,Bye!")
            print("退出程序")
            break
        else:
            print("无效的操作编号，请重新输入")
            print("-"*30)
# 设定程序入口
if __name__ == "__main__":
    main()
```