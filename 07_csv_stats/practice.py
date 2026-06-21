import csv


def read_csv(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        '''
        DictReader 会自动把第一行(表头)作为列名，后续每行数据会被转换成一个字典，键是列名，值是对应单元格的内容。
        例如，如果表头是 "Name,Age,Salary"，后续行是 "Alice,30,70000"，"Bob,25,50000"，
        那么 DictReader 会把第2行转换成 {"Name": "Alice", "Age": "30", "Salary": "70000"}
        第3行会转换成 {"Name": "Bob", "Age": "25", "Salary": "50000"}，以此类推。
        '''
        for row in reader:
            # row 自动是单行字典：{列名:单元格值}
            data.append(row)  # 把单行字典塞进外层列表
    return data


def calculate_stats(data, column_name, cal_type):
    values = []
    # 首先扫描一遍数据判定列值是否能转换成数值
    for row in data:
        # 通过try-except来捕获转换错误，如果某行有问题就跳过该行，否则程序会崩溃
        try:
            # 逐步转换成数值，如果成功就添加到values列表中
            values.append(float(row[column_name]))
        except (ValueError, KeyError):
            continue
    if not values:
        return None
    # 根据cal_type参数来决定计算哪种统计值
    if cal_type == "average":
        return sum(values) / len(values)
    elif cal_type == "max":
        return max(values)
    elif cal_type == "min":
        return min(values)


def main():
    file_path = input("请输入CSV文件路径：")
    # 通过try-except来捕获文件不存在的错误
    # 如果文件路径有误就提示用户并退出程序，否则程序会崩溃
    try:
        data = read_csv(file_path)
    except FileNotFoundError:
        print("文件不存在。")
        return
    if not data:
        print("CSV文件为空。")
        return
    print(f"\n共 {len(data)} 行数据，列名：{list(data[0].keys())}\n")
    column_name = input("请输入要统计的列名(表头)：")
    # 通过判断列名是否在数据的第一行（表头）中来验证用户输入的列名是否有效
    if column_name not in data[0]:
        print(f"列 '{column_name}' 不存在。")
        return
    
    while True:
        cal_type = input("请输入计算类型（average/max/min），输入 exit 退出：")
        if cal_type == "exit":
            break
        if cal_type not in ("average", "max", "min"):
            print("无效类型，请重试。")
            continue
        result = calculate_stats(data, column_name, cal_type)
        if result is None:
            print("该列没有可计算的数值。")
        else:
            print(f"{cal_type}: {result}")
    print("程序结束。")


if __name__ == "__main__":
    main()
