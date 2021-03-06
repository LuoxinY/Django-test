# coding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):
    def parse(self, new_url, html_cont):
    # 利用beautifulSoup 安装指令pip install beautifulsoup4
    # 这个库是解析我们html页面的 帮助我们利用属性抓取标签的 利用它的解析器是html.parser的  encoding是utf8
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls=self.get_new_urls(new_url,soup)
        new_data = self.get_new_data(new_url, soup)
        print new_data
        return new_urls,new_data

    def get_new_urls(self, page_url, soup):
        new_urls=set()  # 定义集合 用于存新urls的
        links=soup.find_all("a",href=re.compile(r"/8hr/page/\d+/"))
        #print links  #[<a href="/8hr/page/2/" rel="nofollow">]
        for link in links:
            part_url=link["href"]
            new_full_url=urlparse.urljoin(page_url,part_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        # 定义字典
        res_data={}
        res_data["title"]=page_url  #存一下url
        user_node=soup.find("div",class_="author clearfix") #这里我没有找所有 是练习一下find 查一个 所以 没一页面爬1个
        user_name=user_node.find_all("a")[1].find("h2").get_text().strip()
        res_data["userName"]=user_name.encode("utf-8") #存一下用户名
         #  抓笑话内容
        joke_content=soup.find("div",class_="content").find("span").get_text().strip()
        res_data["content"] = joke_content.encode("utf-8")  # 存一下笑话
        return res_data
