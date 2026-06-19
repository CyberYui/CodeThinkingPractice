# 07 CSV数据统计

## 目标

读取CSV文件并计算统计信息

## 功能需求

- 读取一个CSV文件
- 显示有哪些列
- 对指定列计算：平均值、最大值、最小值
- 显示统计结果

## 伪代码

在这里写你的伪代码：

```
你的伪代码：
1. 导入必要的库
2. 定义一个函数来读取CSV文件
    # 用户会input file_path
    def read_csv(file_path):
        # 读取CSV文件
        # 确定每一个行列的内容，并存到一个二阶矩阵中
        data = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        # 返回数据
        return data

3. 定义一个函数来计算统计信息
    # 用户会根据需求计算平均值，最大值，最小值
    def calculate_stats(data, row, column, cal_type):
        # 提取指定列的数据
        column_data = [float(row[column]) for row in data[1:]]  # 跳过标题行
        if cal_type == 'average':
            return sum(column_data) / len(column_data)
        elif cal_type == 'max':
            return max(column_data)
        elif cal_type == 'min':
            return min(column_data)
4. 在主函数中调用上述函数并显示结果
    print("请输入CSV文件路径：")
    file_path = input()
    data = read_csv(file_path)
    print("CSV文件的内容是：", data)
    print("接下来输入要计算的行列索引/n")
    row = int(input("请输入行索引："))
    column = int(input("请输入列索引："))
    # 通过一个循环来让用户选择计算类型，当输入exit时退出循环
    while True:
        print("请输入要计算的类型（average/max/min），输入exit推出循环：")
        cal_type = input()
        if cal_type == 'exit':
            break
        result = calculate_stats(data, row, column, cal_type)
        print(f"{cal_type}的结果是：{result}")
```
