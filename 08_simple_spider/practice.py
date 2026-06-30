import urllib.request
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []

    # 抓取网页中的链接
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr, value in attrs:
                if attr == "href" and value:
                    full_url = urljoin(self.base_url, value)
                    self.links.append({"text": "", "url": full_url})

    # 抓取网页中的文本内容
    def handle_data(self, data):
        if self.links and not self.links[-1]["text"]:
            self.links[-1]["text"] = data.strip()


# 使用 urllib.request 发送请求并抓取网页内容
def fetch_links(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"请求失败: {e}")
        return []
    # 使用 LinkExtractor 解析网页内容并提取链接
    parser = LinkExtractor(url)
    # 使用 parser.feed() 方法解析网页内容
    parser.feed(html)
    # 过滤掉没有文本或不是以 http 开头的链接
    return [link for link in parser.links if link["text"] and link["url"].startswith("http")]

# 将抓取到的链接保存到文件中
def save_links(links, filename="results.txt"):
    # 使用 with open() 方法打开文件，并指定编码为 utf-8
    with open(filename, "w", encoding="utf-8") as f:
        for link in links:
            f.write(f"{link['text']}: {link['url']}\n")
    print(f"已保存 {len(links)} 个链接到 {filename}")


def main():
    url = input("请输入网址: ")
    # 如果用户输入的 URL 不以 http 开头，则自动添加 https:// 前缀
    if not url.startswith("http"):
        url = "https://" + url
    print(f"正在抓取: {url}\n")
    links = fetch_links(url)
    if not links:
        print("未找到链接。")
        return
    print(f"共找到 {len(links)} 个链接:\n")
    for i, link in enumerate(links, 1):
        print(f"{i}. {link['text']}: {link['url']}")
    save_links(links)


if __name__ == "__main__":
    main()
