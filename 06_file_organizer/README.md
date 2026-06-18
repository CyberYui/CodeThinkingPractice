# 06 文件整理器

## 目标

自动把文件夹中的文件按扩展名分类

## 功能需求

- 指定一个文件夹路径
- 扫描所有文件
- 按扩展名创建子文件夹（如 .txt → txt文件夹）
- 把文件移动到对应文件夹

## 伪代码

在这里写你的伪代码：

```python
你的伪代码：
    定义一个显示常用文件拓展名的类，用于判断文件后缀属于哪一类
    class FileType:
        def __init__(self):
            self.text = ['.txt', '.md']
            self.image = ['.jpg', '.png', '.gif', '.bmp', '.jpeg']
            self.document = ['.pdf', '.docx', '.xlsx', '.pptx', '.doc', '.xls', '.ppt']
            self.other = ['.zip', '.rar', '.7z', '.tar', '.gz']

    定义一个用于判断类型文件夹是否存在的函数，如果不存在则创建，并把文件移动到对应的文件夹中
    def organize_files(file_type, file):
        判断文件类型，并创建对应的文件夹
        if file_type == 'text':
            type_folder = os.path.join(folder_path, 'Text Files')
            文本文件，判断文本文件夹是否存在，如果不存在则创建，并把文件移动到文本文件夹中
        elif file_type == 'image':
            type_folder = os.path.join(folder_path, 'Image Files')
            图片文件，判断图片文件夹是否存在，如果不存在则创建，并把文件移动到图片文件夹中
        elif file_type == 'document':
            type_folder = os.path.join(folder_path, 'Document Files')
            文档文件，判断文档文件夹是否存在，如果不存在则创建，并把文件移动到文档文件夹中
        else:
            type_folder = os.path.join(folder_path, 'Other Files')
            其他文件，判断其他文件夹是否存在，如果不存在则创建，并把文件移动到其他文件夹中

    def get_folder_path(folder_path):
        获取文件夹中的所有文件，并返回一个文件列表
        files = os.listdir(folder_path)
        for each file in files:
            获取文件的扩展名，并让类型函数分类，把文件移动到对应的文件夹中
            ext = os.path.splitext(file)[1]:
            if ext in file_type.text:
                organize_files('text', file)
            elif ext in file_type.image:
                organize_files('image', file)
            elif ext in file_type.document:
                organize_files('document', file)
            else:
                organize_files('other', file)
    
    定义一个主函数，调用获取文件夹路径的函数
    def main():
        用户需要先输入文件夹路径
        folder_path = input("请输入文件夹路径：")
        调用获取文件夹路径的函数，之后就不用管了，程序会自动把文件分类整理好
        get_folder_path(folder_path)
        当结束后，提示用户文件整理完成
        print("文件整理完成！")

    if __name__ == "__main__":
        main()
```