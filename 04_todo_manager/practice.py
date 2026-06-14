import os

class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        # 硬编码默认未完成状态
        self.completed = False

def show_todo_list(todo_list):
    # 判断待办事项列表是否为空
    if not todo_list:
        print("暂无待办事项")
        return
    for index, item in enumerate(todo_list):
        status = "已完成" if item.completed else "未完成"
        print(f"{index}. {item.title} - {item.description} [{status}]")

def load_todo_list(filename):
    todo_list = []
    if not os.path.exists(filename):
        return todo_list
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            # 判断行数据是否完整，避免因格式问题导致错误
            if len(parts) == 3:
                title, description, completed = parts
                item = TodoItem(title, description)
                # 通过判定读取到的字符串是否为 "True" 来设置 completed，从而形成正确的布尔值
                item.completed = (completed == "True")
                todo_list.append(item)
    return todo_list

def save_todo_list(todo_list, filename):
    with open(filename, "w", encoding="utf-8") as fileline:
        for item in todo_list:
            line = f"{item.title}|{item.description}|{item.completed}\n"
            fileline.write(line)

def add_todo_item(todo_list):
    title = input("请输入待办事项标题：")
    description = input("请输入待办事项描述：")
    item = TodoItem(title, description)
    todo_list.append(item)
    print("添加成功！")

def delete_todo_item(todo_list):
    index = int(input("请输入要删除的待办事项编号："))
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
        print("删除成功！")
    else:
        print("无效的待办事项编号")

def mark_completed(todo_list):
    index = int(input("请输入要标记完成的待办事项编号："))
    if 0 <= index < len(todo_list):
        todo_list[index].completed = True
        print("已标记为完成！")
    else:
        print("无效的待办事项编号")

def main():
    print("欢迎使用待办事项管理器")
    filename = input("请输入想要使用的文件名：") + ".txt"
    todo_list = load_todo_list(filename)

    while True:
        print("-" * 30)
        print("允许操作：1. 添加待办事项 2. 查看所有待办事项 3. 标记完成 4. 删除待办事项 5. 保存文件 6. 退出")
        choice = input("请输入操作编号：")

        if choice == "1":
            add_todo_item(todo_list)
        elif choice == "2":
            print("当前待办事项列表：")
            show_todo_list(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_todo_item(todo_list)
        elif choice == "5":
            save_todo_list(todo_list, filename)
            print("待办事项已保存")
        elif choice == "6":
            save_todo_list(todo_list, filename)
            print("待办事项已保存，Bye!")
            break
        else:
            print("无效的操作编号，请重新输入")

if __name__ == "__main__":
    main()
