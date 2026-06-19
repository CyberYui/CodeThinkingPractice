import csv


def read_csv(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def calculate_stats(data, column_name, cal_type):
    values = []
    for row in data:
        try:
            values.append(float(row[column_name]))
        except (ValueError, KeyError):
            continue
    if not values:
        return None
    if cal_type == "average":
        return sum(values) / len(values)
    elif cal_type == "max":
        return max(values)
    elif cal_type == "min":
        return min(values)


def main():
    file_path = input("请输入CSV文件路径：")
    try:
        data = read_csv(file_path)
    except FileNotFoundError:
        print("文件不存在。")
        return
    if not data:
        print("CSV文件为空。")
        return
    print(f"\n共 {len(data)} 行数据，列名：{list(data[0].keys())}\n")
    column_name = input("请输入要统计的列名：")
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
