import re

# 引入的re模块用于正则表达式匹配，帮助解析Markdown语法
# 对比个人所想，不是直接借用现成的markdown库，而是自己实现一个简单的Markdown解析器，支持标题、列表、加粗、链接和图片等基本语法。
def parse_heading(line):
    # 借助正则表达式匹配 Markdown 标题语法
    # re模块的match函数用于匹配字符串开头的模式，这里匹配以1到6个#开头的行，后面跟着至少一个空格和标题文本
    # \s表示空白字符，+表示匹配一次或多次，.*表示匹配任意字符零次或多次
    match = re.match(r'^(#{1,6})\s+(.*)', line)
    # match函数的结果会返回一个Match对象，如果匹配成功，则可以通过group方法获取匹配的内容
    if match:
        # 获取标题的级别，即#的数量，并将其转换为HTML的<h1>到<h6>标签
        level = len(match.group(1))
        # level保存着每个标题的级别，match.group(2)保存着标题的文本内容
        # 直接输出HTML标签，返回一个字符串
        return f"<h{level}>{match.group(2)}</h{level}>"
    return None

# 解析行内Markdown语法，如加粗、链接和图片
def parse_inline(text):
    # 对于加粗语法，使用正则表达式匹配**包裹的文本，并替换为HTML的<strong>标签
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # 对于链接语法，使用正则表达式匹配[文本](链接)的格式，并替换为HTML的<a>标签
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # 对于图片语法，使用正则表达式匹配![alt](src)的格式，并替换为HTML的<img>标签
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    # 下面是根据生成的markdown文本进一步借鉴添加的代码
    # 对于斜体语法，使用正则表达式匹配*包裹的文本，并替换为HTML的<em>标签
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # 为了区别斜体和加粗，先处理加粗，再处理斜体，避免冲突
    # 对于添加了颜色的文本，使用正则表达式匹配<span style="color:颜色">文本</span>的格式，并替换为HTML的<span>标签
    text = re.sub(r'<span style="color:([^"]+)">(.+?)</span>', r'<span style="color:\1">\2</span>', text)
    # 对于通过``包裹的文本，使用正则表达式匹配`包裹的文本`的格式，并替换为HTML的<code>标签
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # 对于```python```这类代码块语法，使用正则表达式匹配```包裹的文本，并替换为HTML的<pre><code>标签
    text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', text, flags=re.DOTALL)
    return text

# 解析Markdown文本，将其转换为HTML
def parse_markdown(lines):
    # 解析Markdown文本的每一行，生成对应的HTML标签，并将其存储在html_parts列表中
    html_parts = []
    # in_list变量用于标记当前是否在一个无序列表中，初始值为False
    in_list = False
    # in_table变量用于标记当前是否在一个表格中——列表和表格开关必须独立，否则关闭时标签配对错位
    in_table = False
    # list_level记录当前列表缩进级别：1=顶层(- item)，2=嵌套(  - item)，用于多层嵌套列表生成
    list_level = 0

    for line in lines:
        stripped = line.rstrip()
        # 切分每一行的内容，去掉右侧的空白字符，方便后续处理

        # 标题行：关闭所有块级容器（列表/表格），输出标题，跳过后续判断
        heading = parse_heading(stripped)
        if heading:
            if in_list:
                html_parts.append("</ul>" * list_level)
                in_list = False
                list_level = 0
            if in_table:
                html_parts.append("</table>")
                in_table = False
            html_parts.append(heading)
            continue

        # 匹配列表项并捕获前导空格，判断嵌套层级（"  - item"→2级，"- item"→1级）
        # 去掉右侧空白后统计左侧空格数，每2个空格升一级
        leading_spaces = len(stripped) - len(stripped.lstrip())
        current_level = (leading_spaces // 2) + 1
        list_match = re.match(r'^\s*[-*]\s+(.*)', stripped)
        if list_match:
            if in_table:
                html_parts.append("</table>")
                in_table = False
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
                list_level = 1
            # 层级升高时追加新<ul>，层级降低时关闭多余的</ul>
            while list_level < current_level:
                html_parts.append("<ul>")
                list_level += 1
            while list_level > current_level:
                html_parts.append("</ul>")
                list_level -= 1
            html_parts.append(f"<li>{parse_inline(list_match.group(1))}</li>")
            continue

        # 非列表行到达时：关闭所有未闭合的列表层级
        if in_list:
            html_parts.append("</ul>" * list_level)
            in_list = False
            list_level = 0

        # 表格行匹配：以 | 开头和结尾，且中间至少有一个字符
        # 注意：表格开关用 in_table 独立追踪，不能复用 in_list
        table_match = re.match(r'^\|(.+)\|$', stripped)
        if table_match:
            cell_text = table_match.group(1)
            # Markdown 表格分隔行形如 |---|---|：按 | 切分后，每个单元格只含横线/冒号/空格 → 跳过不输出
            raw_cells = [c.strip() for c in cell_text.split('|')]
            if raw_cells and all(re.match(r'^[\s\-:]+$', c) for c in raw_cells):
                continue
            if not in_table:
                html_parts.append("<table>")
                in_table = True
            # 将表格行拆分为单元格，并生成HTML的<tr>和<td>标签
            cells = [cell.strip() for cell in cell_text.split('|')]
            html_parts.append("<tr>" + "".join(f"<td>{parse_inline(cell)}</td>" for cell in cells) + "</tr>")
            continue

        # 不在列表也不在表格的非空行 → 表格已关闭，只处理段落
        if in_table:
            html_parts.append("</table>")
            in_table = False

        # 解析普通段落，将其转换为HTML的<p>标签
        if stripped:
            html_parts.append(f"<p>{parse_inline(stripped)}</p>")
        elif html_parts and html_parts[-1] != "<p></p>":
            pass

    # 文件结束时确保列表和表格都闭合，否则最后一个块级元素会悬空
    if in_list:
        html_parts.append("</ul>" * list_level)
    if in_table:
        html_parts.append("</table>")

    return "\n".join(html_parts)


def main():
    # 从命令行参数获取输入文件路径，如果没有提供，则提示用户输入
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else input("请输入md文件路径: ")
    # 读取Markdown文件的内容，并将其按行存储在lines列表中
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    body = parse_markdown(lines)
    # 将解析后的HTML内容嵌入到完整的HTML文档结构中，包括<!DOCTYPE html>声明、<html>、<head>和<body>标签
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{input_file}</title>
</head>
<body>
{body}
</body>
</html>"""

    # 将生成的HTML内容写入到输出文件中，输出文件名与输入文件名相同，但扩展名为.html
    output_file = input_file.rsplit(".", 1)[0] + ".html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"已输出: {output_file}")


if __name__ == "__main__":
    main()
