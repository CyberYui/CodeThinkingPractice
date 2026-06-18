import os
import shutil


class FileType:
    def __init__(self):
        self.categories = {
            "Text Files": [".txt", ".md"],
            "Image Files": [".jpg", ".png", ".gif", ".bmp", ".jpeg"],
            "Document Files": [".pdf", ".docx", ".xlsx", ".pptx", ".doc", ".xls", ".ppt"],
            "Other Files": [".zip", ".rar", ".7z", ".tar", ".gz"],
        }

    # 根据文件扩展名返回对应的分类，这里传入了查询的扩展名，并且将其转换为小写以确保匹配的准确性。
    # 如果找不到匹配的分类，则返回 "Other Files"。
    def get_category(self, extension):
        # items() 方法作为字典的经典方法，返回每一个键值对，在这里就是 键:列表 对
        # 由于设定了两个循环变量，所以在每次迭代中：
        # folder_name 将会是当前的键（分类名称）
        # extensions 将会是当前键对应的值（扩展名列表）
        for folder_name, extensions in self.categories.items():
            # extension.lower() 将输入的扩展名转换为小写，以确保与列表中的扩展名进行比较时不受大小写影响。
            if extension.lower() in extensions:
                return folder_name
        return "Other Files"


def organize_files(folder_path, file_type):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if not os.path.isfile(filepath):
            continue
        _, ext = os.path.splitext(filename)
        category = file_type.get_category(ext)
        # dest_folder 就是 destination folder 的缩写
        dest_folder = os.path.join(folder_path, category)
        '''makedirs函数实际做的事
        def makedirs(path, exist_ok=False):
        if 文件夹不存在:
            创建文件夹()
        else:
            # 文件夹已存在，此时才看exist_ok
            if not exist_ok:
                raise FileExistsError  # 报错
            else:
                pass  # 啥也不干，直接放行
        '''
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(filepath, os.path.join(dest_folder, filename))
        print(f"  {filename} → {category}/")


def main():
    folder_path = input("请输入文件夹路径：")
    if not os.path.isdir(folder_path):
        print("路径无效或不是文件夹。")
        return
    file_type = FileType()
    print(f"\n正在整理：{folder_path}\n")
    organize_files(folder_path, file_type)
    print("\n文件整理完成！")


if __name__ == "__main__":
    main()
