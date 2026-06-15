import os
from datetime import datetime


class DiaryEntry:
    def __init__(self, content):
        # 借助datetime模块获取当前日期和时间，并格式化为字符串
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.content = content


def save_diary(entry, folder="diary"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = entry.date.split(" ")[0] + ".txt"
    filepath = os.path.join(folder, filename)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"[{entry.date}]\n{entry.content}\n\n")


def view_history(folder="diary"):
    if not os.path.exists(folder):
        print("暂无日记记录。")
        return None
    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    if not files:
        print("暂无日记记录。")
        return None
    files.sort()
    print("\n历史日记列表：")
    for index, filename in enumerate(files, start=1):
        print(f"{index}. {filename}")
    return files


def view_specific_date(choice=None, folder="diary"):
    if choice is not None:
        files = view_history(folder)
        if not files:
            return
        if 1 <= choice <= len(files):
            filepath = os.path.join(folder, files[choice - 1])
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"\n{content}")
        else:
            print("无效的编号。")
    else:
        date_input = input("请输入要查看的日记日期（格式：YYYY-MM-DD）：")
        filepath = os.path.join(folder, f"{date_input}.txt")
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"\n{content}")
        else:
            print("没有找到该日期的日记！")


def new_diary():
    content = input("请输入新日记的内容：")
    if not content.strip():
        print("日记内容不能为空。")
        return
    entry = DiaryEntry(content)
    save_diary(entry)
    print("日记已保存！")


def main():
    print("欢迎使用日记本！")
    while True:
        print("\n请选择操作：")
        print("1. 新建日记")
        print("2. 查看历史日记")
        print("3. 查看指定日期的日记")
        print("4. 退出")
        choice = input("请输入选项（1-4）：")
        if choice == "1":
            new_diary()
        elif choice == "2":
            files = view_history()
            if files:
                sub_choice = input("请输入要查看的日记编号（按回车跳过）：")
                if sub_choice.isdigit():
                    view_specific_date(int(sub_choice))
        elif choice == "3":
            view_specific_date()
        elif choice == "4":
            print("感谢使用日记本，再见！")
            break
        else:
            print("无效的选择，请重新输入！")


if __name__ == "__main__":
    main()
