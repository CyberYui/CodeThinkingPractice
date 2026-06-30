# 08 简单爬虫

## 目标

抓取网页的标题和链接

## 功能需求

- 输入一个网址
- 抓取页面中的所有链接
- 显示链接文本和URL
- 保存结果到文件

## 伪代码

在这里写你的伪代码：

```
你的伪代码：
    从用户输入获取网址
    webpage = input("请输入网址: ")
    # 参考人类访问网页的形式访问网页
    获取网页内容，如果网页是瀑布流网页，则只读取第一页内容
    解析网页内容，提取所有链接
    对每个链接：
        获取链接文本和URL，并放到一个列表字典中
        links.append({"text": link_text, "url": link_url})
        显示链接文本和URL在终端中
        print(f"当前网页一共有 {len(links)} 个链接，列表如下：")
        print(f"链接文本: {link_text}, 链接URL: {link_url}")
    将结果保存到文件
    with open("结果.txt", "w", encoding="utf-8") as f:
        # 首先判断文件是否存在
        if os.path.exists("结果.txt"):
            print("文件已存在，正在覆盖...")
            # 覆盖前先清空文件内容
            f.truncate(0)
        for link in links:
            f.write(f"链接文本: {link['text']}, 链接URL: {link['url']}\n")
